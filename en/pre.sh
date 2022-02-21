#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

TARGET=$1
LANGUAGE=$2
echo "Processing PRE TARGET=$TARGET LANGUAGE=$LANGUAGE"

FILE_CONT=contents.rst
SANSKRIT_LIST=$LANGUAGE/sed_RESULT.txt

if [ $TARGET == 'latexpdf' ] || [ $TARGET == 'html' ] ||[ $TARGET == 'epub' ]; then

    for F in conf.py contents.rst genindex.rst glossary.rst index.rst style.tex.txt
    do
        cp $LANGUAGE/$F .
    done

    sed -i -f $LANGUAGE/PreprocessorPatterns.sed ${FILE_CONT}

    if [ -f "$SANSKRIT_LIST" ]; then
        echo "Create Indices for Sanskrit from file: $SANSKRIT_LIST"
        while read STR; do

            # Below is an example of Sanskrit line with Diacritic text:
            # *сампрада̄йа-вихӣна̄ йе*
            # 1..6 spaces before Diacritic text. Fix if it is needed more.

            # old variant: insert "after":
            #s/^\( *\).*/&\n\n\1.. index:: '"$STR"'\n/' ${FILE_CONT}

            echo "   Processing: $STR"
            sed -i '/^[ ]\{1,6\}\*'"$STR"'\*$/ !b
s/^\( *\).*/\1.. index:: '"$STR"'\n\n&\n/' ${FILE_CONT}

        done <$SANSKRIT_LIST
    fi

    # Exceptions:
    # **маха̄-бха̄гавата**-*ш́решт̣хо бра̄хман̣о ваи гурур нр̣н̣а̄м*
    # *маха̄-кула-прасӯто ’пи сарва-йаджн̃ешу*\ **дӣкшитах̣**
    sed -i '/^[ ]\{1,6\}\*маха̄-кула-прасӯто ’пи сарва-йаджн̃ешу\*/ !b
s/^\( *\).*/\1.. index:: маха̄-кула-прасӯто ’пи сарва-йаджн̃ешу дӣкшитах̣\n\n&\n/' ${FILE_CONT}
    sed -i '/^[ ]\{1,6\}\*\*маха̄-бха̄гавата\*\*-\*ш́решт̣хо бра̄хман̣о ваи гурур нр̣н̣а̄м\*$/ !b
s/^\( *\).*/\1.. index:: маха̄-бха̄гавата-ш́решт̣хо бра̄хман̣о ваи гурур нр̣н̣а̄м\n\n&\n/' ${FILE_CONT}

    # Fix path to fonts in configuration file:
    sed -i 's|^\([ ]*\)Path = \./fonts/\(.*\)$|\1Path = '"${PWD}"'/fonts/\2|g' ./conf.py
fi


if [ $TARGET == 'epub' ]; then
    echo "  Processing: EPUB"
    DIR=_static

    rm -f ${DIR}/CharisSIL-*.otf
    rm -f ${DIR}/CharisSIL-*.ttf
    #rm -f ${DIR}/CharisSIL-*.woff
    rm -f ${DIR}/CharisSIL-*.woff2
    rm -f ${DIR}/favicon*.ico
    rm -f ${DIR}/CharisSIL-webfont.css
    rm -f ${DIR}/epub-cover.xhtml
    
    rm -f glossary.rst
    rm -f genindex.rst
    # Fix warnings about Menu:
    sed -i '/^[ ]*genindex$/d' ./index.rst
    sed -i '/^[ ]*glossary$/d' ./index.rst
fi


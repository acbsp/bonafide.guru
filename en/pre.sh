#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

TARGET=$1
LANGUAGE=$2
echo "Processing PRE TARGET=$TARGET LANGUAGE=$LANGUAGE"

FILE_CONT=$LANGUAGE/contents.rst
SANSKRIT_LIST=$LANGUAGE/sed_RESULT.txt

if [ $TARGET == 'latexpdf' ] || [ $TARGET == 'latex' ]  || [ $TARGET == 'html' ] || [ $TARGET == 'epub' ]; then

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

    # Fix path to fonts in configuration file for LaTeX:
    sed -i 's|^\([ ]*\)Path = \./fonts/\(.*\)$|\1Path = '"${PWD}/${LANGUAGE}"'/fonts/\2|g' $LANGUAGE/conf.py
fi


if [ $TARGET == 'html' ]; then
    FROMDIR=$LANGUAGE/_static
    TODIR=$LANGUAGE/_extra/_static/css/fonts

    mkdir -p ${TODIR} 
    
    cp ${FROMDIR}/CharisSIL-Bold.woff   ${TODIR}/Roboto-Slab-Bold.woff
    cp ${FROMDIR}/CharisSIL-Bold.woff2  ${TODIR}/Roboto-Slab-Bold.woff2
    cp ${FROMDIR}/CharisSIL-Regular.woff   ${TODIR}/Roboto-Slab-Regular.woff
    cp ${FROMDIR}/CharisSIL-Regular.woff2  ${TODIR}/Roboto-Slab-Regular.woff2

    mv ${FROMDIR}/CharisSIL-Bold.woff  ${TODIR}/lato-bold.woff
    mv ${FROMDIR}/CharisSIL-Bold.woff2 ${TODIR}/lato-bold.woff2
    mv ${FROMDIR}/CharisSIL-Italic.woff  ${TODIR}/lato-normal-italic.woff
    mv ${FROMDIR}/CharisSIL-Italic.woff2 ${TODIR}/lato-normal-italic.woff2
    mv ${FROMDIR}/CharisSIL-Regular.woff  ${TODIR}/lato-normal.woff
    mv ${FROMDIR}/CharisSIL-Regular.woff2 ${TODIR}/lato-normal.woff2
    mv ${FROMDIR}/CharisSIL-BoldItalic.woff  ${TODIR}/lato-bold-italic.woff
    mv ${FROMDIR}/CharisSIL-BoldItalic.woff2 ${TODIR}/lato-bold-italic.woff2

    chmod 444 ${TODIR}/*

    date >> ${TODIR}/test.txt
fi


if [ $TARGET == 'epub' ]; then
    echo "  Processing: EPUB"
    DIR=$LANGUAGE/_static

    rm -f ${DIR}/CharisSIL-*.otf
    rm -f ${DIR}/CharisSIL-*.ttf
    #rm -f ${DIR}/CharisSIL-*.woff
    rm -f ${DIR}/CharisSIL-*.woff2
    rm -f ${DIR}/favicon*.ico
    rm -f ${DIR}/CharisSIL-webfont.css
    rm -f ${DIR}/epub-cover.xhtml
    
    rm -f $LANGUAGE/glossary.rst
    rm -f $LANGUAGE/genindex.rst
    # Fix warnings about Menu:
    sed -i '/^[ ]*genindex$/d' $LANGUAGE/index.rst
    sed -i '/^[ ]*glossary$/d' $LANGUAGE/index.rst
fi


#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

TARGET=$1
LANGUAGE=$2
FILE_CONT=contents.rst
SANSKRIT_LIST=$LANGUAGE/sed_RESULT.txt

echo "Processing PRE TARGET=$TARGET LANGUAGE=$LANGUAGE"

# for all targets

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
s/^\( *\).*/\n\1.. index:: '"$STR"'\n&\n/' ${FILE_CONT}

        done <$SANSKRIT_LIST
    fi
fi


if [ $TARGET == 'epub' ]; then
       echo "   Processing: EPUB"
fi


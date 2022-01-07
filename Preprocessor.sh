#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

FILENAME=contents.rst
SANSKRIT_LIST=sed_RESULT.txt

TMPORIG=$(mktemp /tmp/${FILENAME}.XXXXXXXXX)

cp ${FILENAME} ${TMPORIG}

cp ${FILENAME} ${FILENAME}_ORIG
cat ${FILENAME}_ORIG | sed --file PreprocessorPatterns.sed > ${FILENAME}


if [ -f "$SANSKRIT_LIST" ]; then
    echo "Create Indices for Sanskrit from file: $SANSKRIT_LIST"
    while read STR; do

#      Below is an example of Sanskrit line with Diacritic text:
# *сампрада̄йа-вихӣна̄ йе*
       # 1..6 spaces before Diacritic text. Fix if it is needed more.

       echo "Processing: $STR"
#      sed -i '/'"$STR"'/a\\n.. index:: '"$STR"'\n\n..\n'  ${FILENAME}

       sed -i '/^[ ]\{1,6\}\*'"$STR"'\*$/ !b
s/^\( *\).*/&\n\n\1.. index:: '"$STR"'\n/' ${FILENAME}

    done <$SANSKRIT_LIST
fi



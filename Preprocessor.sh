#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

FILENAME=contents.rst
TMPORIG=$(mktemp /tmp/${FILENAME}.XXXXXXXXX)

cp ${FILENAME} ${TMPORIG}

cp ${FILENAME} ${FILENAME}_ORIG
cat ${FILENAME}_ORIG | sed --file PreprocessorPatterns.sed > ${FILENAME}





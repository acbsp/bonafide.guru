#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

DIR=_build/epub
FILE=contents.xhtml 

cd $DIR
echo "    Processing file: $FILE"
# <p class="attribution">—Нектар преданности, Введение</p>
sed -i 's%<p class="attribution">—\(.*\)</p>%<p class="attribution">(\1)</p>%' ${FILE}

# add second ':'
sed -zE 's%(</dt>[^\n]*\n[^\n]*<p>:)% :\1%Mg' -i ${FILE}
# remove first ':'
sed -i 's%<p>: %<p>%g' ${FILE}

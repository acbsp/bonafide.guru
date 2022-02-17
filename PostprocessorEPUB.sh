#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

DIR=_build/epub
FILE_X=contents.xhtml 

cd $DIR
echo "    Processing file: $FILE_X"
# <p class="attribution">—Нектар преданности, Введение</p>
sed -i 's%<p class="attribution">—\(.*\)</p>%<p class="attribution">(\1)</p>%' ${FILE_X}
# <p class="attribution" id="index-30">—Падма Пура̄н̣а</p>
sed -i 's%\(<p class="attribution" id="index-[0-9]*">\)—\(.*\)</p>%\1(\2)</p>%' ${FILE}

# add second ':'
sed -zE 's%(</dt>[^\n]*\n[^\n]*<p>:)% :\1%Mg' -i ${FILE_X}
# remove first ':'
sed -i 's%<p>: %<p>%g' ${FILE_X}

#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

DIR=_static

rm -f glossary.rst
rm -f genindex.rst

rm -f ${DIR}/CharisSIL-*.otf
rm -f ${DIR}/CharisSIL-*.ttf
#rm -f ${DIR}/CharisSIL-*.woff
rm -f ${DIR}/CharisSIL-*.woff2
rm -f ${DIR}/favicon*.ico
rm -f ${DIR}/custom.css
rm -f ${DIR}/CharisSIL-webfont.css
#rm -f ${DIR}/

#cd _build/html
#for STR in contents.html genindex.html glossary.html index.html search.html
#do
#    echo "    Processing file: $STR"
#    sed -i 's/placeholder="Поиск в документации"/placeholder="Поиск в книге"/'  ${STR}
#done


#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

FILE=contents.html 
FROMDIR=_build/html/_static
TODIR=_build/html/_static/css/fonts

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


cd _build/html

for STR in contents.html genindex.html glossary.html index.html search.html
do
    echo "    Processing file: $STR"
    sed -i 's/placeholder="Поиск в документации"/placeholder="Поиск в книге"/'  ${STR}
done

echo "    Processing file: $FILE"
# <p class="attribution">—Нектар преданности, Введение</p>
sed -i 's%<p class="attribution">—\(.*\)</p>%<p class="attribution">(\1)</p>%' ${FILE}
# <p class="attribution" id="index-30">—Падма Пура̄н̣а</p>
sed -i 's%\(<p class="attribution" id="index-[0-9]*">\)—\(.*\)</p>%\1(\2)</p>%' ${FILE}

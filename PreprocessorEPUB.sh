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

# Fix warnings about Menu:
sed -i '/^[ ]*genindex$/d' ./index.rst
sed -i '/^[ ]*glossary$/d' ./index.rst

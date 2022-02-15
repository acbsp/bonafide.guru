#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

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


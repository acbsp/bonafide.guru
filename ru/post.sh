#!/bin/bash - 
set -o nounset                              # Treat unset variables as an error

TARGET=$1
LANGUAGE=$2

echo "Processing POST TARGET=$TARGET LANGUAGE=$LANGUAGE"

# for all targets

if [ $TARGET == 'latexpdf' ] || [ $TARGET == 'html' ] ||[ $TARGET == 'epub' ]; then
    echo "    Processing test"
fi


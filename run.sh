#! /bin/bash

set -e

if [ ! -f "$1" ]; then
    echo "$1 does not exists."
    exit 1
fi

export DB_PATH="$1" && flask --app flaskapp.app run --host 0.0.0.0 --port "$2"
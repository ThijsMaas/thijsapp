#! /bin/bash

set -e

DBFILE=/data/db.txt
if [ ! -f "$FILE" ]; then
    echo "$FILE does not exists."
    exit 1
fi

flask --app flaskapp.app run
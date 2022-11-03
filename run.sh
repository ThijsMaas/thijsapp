#! /bin/bash

set -e

DBFILE=/data/db.txt

if [ ! -f "$DBFILE" ]; then
    echo "$DBFILE does not exists."
    exit 1
fi

export DB_PATH=$DBFILE && flask --app flaskapp.app run
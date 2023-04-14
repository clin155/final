#!/bin/bash

set -Eeuo pipefail
set -x

usage() {
    echo "Usage: $0 (create|destroy|reset|view)"
}

if [ $# -ne 1 ]; then
    usage
    exit 1
fi

case $1 in
    "create")

        if test -f database.sqlite3; then
            :
        else
            sqlite3 database.sqlite3 < schema.sql
        fi
        ;;
    "destroy")
        rm -rf database.sqlite3
    ;;
    "reset")
        rm -rf database.sqlite3
        sqlite3 database.sqlite3 < schema.sql
    ;;
    "view")
        sqlite3 -batch -line database.sqlite3
    ;;
    *)
        usage
        exit 1
    ;;
esac
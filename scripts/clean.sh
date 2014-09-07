#!/bin/sh
FROM=utf-8
TO=ascii
FILE=data/raw/asa_2014_prelim.csv
OUT=data/clean_asa_2014_prelim.csv

iconv -c -f $FROM -t $TO $FILE > $OUT

echo "Done cleaning $FILE!"

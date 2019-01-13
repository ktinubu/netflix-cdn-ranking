#!/bin/sh

git pull
python3 adddata.py rankings.pk
python3 writedata.py rankings.csv rankings.pk
rm rankings.pk
git add .
git commit -m "manifest update from ${NFLIXLOCATION}"
git push 
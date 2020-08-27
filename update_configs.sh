#!/bin/bash

idir=$PWD

for d in *-feedstock; do
    cd $d
    echo "Feedstock: $d"
    git checkout master
    git pull --all
    cp ../event-model-feedstock/conda-forge.yml .
    git add .
    git commit -m '`channel_priority: flexible` config in conda-forge.yml'
    git push
    cd $idir
    echo -e "\n\n"
done

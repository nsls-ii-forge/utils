#!/bin/bash

script_dir=$(dirname $0)
echo $script_dir

for i in $(python ${script_dir}/get_all_feedstocks.py); do
    dirname=$(echo $i | awk -F/ '{print $5}')  # parse the GH url
    echo "Dirname: $dirname"
    if [ ! -d "$dirname" ]; then
        git clone $i
    fi
done

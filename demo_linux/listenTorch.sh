#!/bin/bash
inotifywait -m /data/home/winfredsun/demo/image -e create |
    while read path action file; do
        echo "The file '$file' appeared in directory '$path' via '$action'"
        bash predict.sh
        rm /data/home/winfredsun/demo/image/$file
    done


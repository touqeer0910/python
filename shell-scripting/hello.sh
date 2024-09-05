#!/bin/bash
result=0
for index in {1..999}; do
    #echo "$index"
    if [[ $(( index%3 )) == 0  || $(( index%5 )) == 0  ]]; then
         result=$((result+index))
    fi
done
     echo $result
     


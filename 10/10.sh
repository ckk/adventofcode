#!/bin/sh

for s in 40 50; do
    inp=1113122113
    for i in `seq $s`
    do
        inp=`echo -n $inp | sed -r "s/(.)/\\1\n/g" | uniq -c | tr -d '\n\t '`
    done
    echo -n $inp | wc -c
done

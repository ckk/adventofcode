#!/usr/bin/env python

import json

# my first solution for counting all numbers was a really quick and dirty method in the shell:
#  jq . < input | egrep '[[:digit:]]+' | sed -re #  's/^[^[:digit:]-]*([-[:digit:]]+)[^-[:digit:]]*$/\1/'
# which gives all of the numbers, then another simple one-liner to sum them. 
# Both the sum and the filter in part two should be possibly to do by just using jq, if you're good
# at it. :)
def count_all(d, no_red):
    s = 0
    if type(d) == dict:
        vals = d.values()
        if no_red and 'red' in vals:
            return 0
    elif type(d) == list:
        vals = d
    s += sum([v if type(v) == int else 0 for v in vals])
    for v in vals:
        if type(v) == dict:
            s += count_all(v, no_red)
        if type(v) == list:
            s += count_all(v, no_red)
    return s

def do(input_file):
    with open(input_file) as f:
        doc = json.load(f)
    print count_all(doc, False)
    print count_all(doc, True)

do('input')


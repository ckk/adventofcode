#!/usr/bin/env python

import re

def do(input_file):
    with open(input_file) as f:
        strings = [s.strip() for s in f.readlines()]
    orig_size, decoded_size = 0,0
    for s in strings:
        orig_size += len(s)
        d = eval(s)
        decoded_size += len(d)
    print "diff:", orig_size - decoded_size
    exploded_size = 0
    for s in strings:
        e = re.escape(s)
        exploded_size += len(e) + 2
    print "diff 2:", exploded_size - orig_size

do('input-test')
do('input')


#!/usr/bin/env python

from hashlib import md5

def find(l):
    hash = ''
    number = 0
    zeros = '0' * l
    while hash[:l] != zeros:
        number += 1
        hash = md5('iwrupvqb%d' % number).hexdigest()
    print number

find(5)
find(6)

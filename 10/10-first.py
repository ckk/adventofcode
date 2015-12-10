#!/usr/bin/env python

import re

def do(inp):
    out = ''
    last = ''
    count = 0
    for c in inp:
        if last == '':
            last = c
            count = 1
            continue
        if last != c:
            out += str(count)
            out += last
            last = c
            count = 1
            continue
        if last == c:
            count += 1
    out += str(count)
    out += last
    return out

print do('1')
print do('11')
print do('21')
print do('1211')
print do('1112211')
inp = '1113122113'
for i in range(40):
    inp = do(inp)
print len(inp)
inp = '1113122113'
for i in range(50):
    inp = do(inp)
print len(inp)

#!/usr/bin/env python

from itertools import groupby

def pw_ok(pw):
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False
    if sum([1 if len(list(it)) > 1 else 0 for what, it in groupby(pw)]) < 2:
        return False
    for i in range(0,6):
        if (ord(pw[i+1]) - ord(pw[i]) == 1 and
            ord(pw[i+2]) - ord(pw[i+1]) == 1):
            return True
    return False

def increase(pw, pos):
    pw[pos] = chr(ord(pw[pos]) + 1)
    if pw[pos] == '{':
        pw[pos] = 'a'
        return increase(pw, pos-1)
    else:
        return pw
    
def do(pw):
    pw = list(pw)
    while not pw_ok(pw):
        pw = increase(pw, 7)
    return ''.join(pw)

print do('abcdefgh')
print do('ghijklmn')
first = do('hxbxwxba')
print first
print do(''.join(increase(list(first), 7)))

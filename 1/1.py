#!/usr/bin/env python

with open("input") as f:
    input = f.read().strip()
    print input.count('(') - input.count(')')

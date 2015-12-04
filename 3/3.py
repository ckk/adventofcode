#!/usr/bin/env python

from collections import defaultdict

def house_visits(input):
    houses = defaultdict(lambda: 0)
    hx, hy = 0, 0
    houses['0:0'] = 1
    with open(input) as f:
        input = f.read().strip()
        for c in input:
            if c == '<':
               hx -= 1
            elif c == '>':
               hx += 1
            elif c == '^':
               hy += 1
            elif c == 'v':
               hy -= 1
            houses['%s:%s' % (hx, hy)] += 1
        return len(houses)
        
def move(c, x, y):
    if c == '<':
       x -= 1
    elif c == '>':
       x += 1
    elif c == '^':
       y += 1
    elif c == 'v':
       y -= 1
    return x, y

def house_visits_b(input):
    houses = defaultdict(lambda: 0)
    sx, sy = 0, 0
    rx, ry = 0, 0
    houses['0:0'] = 2
    with open(input) as f:
        input = f.read().strip()
        for i, c in enumerate(input):
            if i % 2 == 0:
                sx, sy = move(c, sx, sy)
                houses['%s:%s' % (sx, sy)] += 1
            else:
                rx, ry = move(c, rx, ry)
                houses['%s:%s' % (rx, ry)] += 1

        return len(houses)

print('a test_input_1: {}'.format(house_visits('test_input_1')))
print('a test_input_2: {}'.format(house_visits('test_input_2')))
print('a test_input_3: {}'.format(house_visits('test_input_3')))
print('a input: {}'.format(house_visits('input')))
print('b test_input_1b: {}'.format(house_visits_b('test_input_1b')))
print('b test_input_2: {}'.format(house_visits_b('test_input_2')))
print('b test_input_3: {}'.format(house_visits_b('test_input_3')))
print('b input: {}'.format(house_visits_b('input')))

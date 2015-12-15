#!/usr/bin/env python

import re
from itertools import ifilter, product, repeat

def do(input_file, calories):
    with open(input_file) as f:
        strings = [s.strip() for s in f.readlines()]
    ingredients = list()
    ingredients_cals = list()
    for s in strings:
        properties = [int(i) for i in re.findall(r"[\d-]+", s)]
        ingredients.append(properties[:-1])
        ingredients_cals.append(properties[-1])
    max_cookie = 0
    max_cookie_with_cal = 0
    for cookie in ifilter(lambda t: sum(t) == 100, product(*repeat(range(1,100), len(ingredients)))):
        cookie_score = reduce(lambda a, b: a*b, 
            [0 if score < 0 else score for score in [sum(map(lambda x: reduce(lambda a, b: a*b, x), zip(cookie, p))) for p in zip(*ingredients)]]
        )
        max_cookie = max(max_cookie, cookie_score)
        if sum(map(lambda x: reduce(lambda a, b: a*b, x), zip(cookie, ingredients_cals))) == calories:
            max_cookie_with_cal = max(max_cookie_with_cal, cookie_score)
    print max_cookie, max_cookie_with_cal
do('input-test', 500)
do('input', 500)

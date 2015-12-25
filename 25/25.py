#!/usr/bin/env python27

INITIAL_VALUE= 20151125

# brute force again, bothing clever at all
def code(row, column):
    val = 0
    this_row = 1 # the bottom left of this diagonal
    while True:
        r = this_row
        c = 1
        while r > 0:
            if r == 1 and c == 1:
                val = INITIAL_VALUE
            else:
                val = val * 252533 % 33554393
            if r == row and c == column:
                return val
            r -= 1
            c += 1
        this_row += 1
    
#print code(6, 2)
#print code(6, 6)
print code(2981, 3075)

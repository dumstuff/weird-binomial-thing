#!/usr/bin/python

from sympy import *

maxx = 100
for y in range(1, maxx):
	for x in range(1, maxx):
		if not sum(binomial(x, i)*binomial(y-1, i-1) for i in range(1, min(x,y)+1)) == binomial(x+y-1, min(x-1, y)):
			print 'shit'

#!/usr/bin/python

from sympy import *

def sequences(maxx, maxlen):
	if maxlen == 0:
		return [[]]
	ret = []
	for i in range(1, maxx+1):
		ret.extend([[i] + ar for ar in sequences(i, maxlen-1)])
	return ret

def sequences2(maxx, maxlen):
	if maxlen == 0:
		return [[]]
	ret = []
	for i in range(maxx+1):
		ret.extend([[i] + ar for ar in sequences2(i, maxlen-1)])
	return ret

def weird_binomial(maxj, maxk):
    box = [[0]*maxk for _ in range(maxj)]
    for j in range(maxj):
    	for k in range(maxk):
    		ar = sequences(j, k)
    		#for i in ar: print i
    		maxx = j
    		length = k
    		sumthing = sum(binomial(maxx, i)*binomial(length-1, i-1) for i in range(1, min(length+1, maxx+1)))
    		box[j][k] = (len(ar) == binomial(j+k-1, min(j-1,k)))
    	if False in box[j]:
    		print 'shit'
    	else:	
    		print box[j]

def product_thing(seq, primes):
	prod = 1
	for s,p in zip(seq, primes):
		prod *= p**s
	return prod

def divisors(seq):
	prod = 1
	for s in seq:
		prod *= (s+1)
	return prod

def oeis(maxx, length):
	ar = sequences2(maxx, length)
	primes = list(primerange(1, length*10))
	numbers = [(product_thing(seq, primes), divisors(seq)) for seq in ar]
	numbers.sort(key=lambda pair: pair[0])
	the_sequence = []
	maxdiv = 0
	for n,div in numbers:
		if div > maxdiv:
			the_sequence.append(n)
			maxdiv = div
	return the_sequence
	

#weird_binomial(20, 5)
print oeis(20, 5)

#for i in sequences(10, 4): print i
#for i in box:
#	print i

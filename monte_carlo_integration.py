import numpy as np
import sys
from scipy import optimize as op

#makes life easier later on
def evaluate(x):
	return (np.exp(x * x))

#define a stochastic analyzer because it's more fun
def random_optimize(maximum, a, b):

	initial = maximum

	#using a sample size of 10000
	for i in range(10000):
		#generate the random value
		x = (b-a)* np.random.random_sample() + a
		f_x = evaluate(x)

		if f_x > maximum + 0.1: #define an error tolerance of 0.1
			maximum = f_x

	#if we found a better guess
	if initial != maximum:
		random_optimize(2*maximum, a, b)
	else:
		return 2*maximum #scale by a factor of 2 to be safe.

def monte_integrate(a, b, N):

	hits = 0

	#evaluate the endpoints outside of the recursive loop
	max_ab = max(evaluate(a), evaluate(b))

	f_max = random_optimize(max_ab, a, b)

	print(f_max)
	for i in range(N):

		#generate the random x value
		x = (b-a)* np.random.random_sample() + a
		y = f_max*np.random.random_sample()
		f_x = evaluate(x)

		if y <= f_x:
			hits += 1

		print("The integral is approximately: " + str(float(hits / (i+ 1)) * ((b-a) * f_max)) + " after " + str(i) + " samples.", end='\r')

try:
	monte_integrate(float(sys.argv[1]), float(sys.argv[2]), 10 ** int(sys.argv[3]))
	print("")
except:
	print("")
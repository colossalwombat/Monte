import sys, re
import numpy as np
from scipy import optimize as op

#function to be integrated
def evaluate(function, x):
    return float(eval(function))

#define a stochastic analyzer because it's more fun
def random_optimize(function, maximum, a, b):

    initial = maximum

    #using a sample size of 10000
    for i in range(10000):
        #generate the random value
        x = (b-a)* np.random.random_sample() + a
        f_x = evaluate(function, x)

        if f_x > maximum + 0.1: #define an error tolerance of 0.1
            maximum = f_x

    #if we found a better guess
    if initial != maximum:
        random_optimize(function, 1.1*maximum, a, b)
    else:
        return 1.1*maximum #scale by a factor of 1.1 to be safe.

def parse_input(input_string):

    #replaces text inputs as their numpy equivalents
    input_string = input_string.replace('e', 'np.e')
    input_string = input_string.replace('pi', 'np.pi')
    input_string = input_string.replace('^', '**')
    input_string = input_string.replace('sin', 'np.sin')
    input_string = input_string.replace('cos', 'np.cos')
    input_string = input_string.replace('arctan', 'np.arctan')
    input_string = input_string.replace('arccos', 'np.arccos')

    return input_string

def monte_integrate(function, a, b,  N):

    hits = 0

    #evaluate the endpoints outside of the recursive loop
    max_ab = max(evaluate(function, a), evaluate(function, b))

    f_max = random_optimize(function, max_ab, a, b)

    print("The maximum value of f on [a,b] is approximately: " + str(f_max))

    for i in range(N):

        #generate the random x value
        x = (b-a)* np.random.random_sample() + a
        y = f_max*np.random.random_sample()
        f_x = evaluate(function, x)

        if y <= f_x:
            hits += 1

        print("The integral is approximately: " + str(float(hits / (i+ 1)) * ((b-a) * f_max)) + " after " + str(i) + " samples.      ", end='\r')


function= parse_input(str(sys.argv[1]))
print("The function to integrate was parsed into numpy format as " + str(function))
monte_integrate(function, float(sys.argv[2]), float(sys.argv[3]),  10 ** int(sys.argv[4]))
print("")

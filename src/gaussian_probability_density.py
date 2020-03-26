# step 4 - gaussian_probability_density.py

from math import sqrt
from math import pi 
from math import exp

def calculate_probability(x, mean, stdev):
	exponent = exp(-((x-mean)**2 / (2 * stdev**2)))
	return (1 / (sqrt(2 * pi) * stdev)) * exponent


if __name__ == '__main__':
	print(calculate_probability(1.0, 1.0, 1.0))
	print(calculate_probability(2.0, 1.0, 1.0))
	print(calculate_probability(0.0, 1.0, 1.0))
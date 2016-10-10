from math import pi, cos, sqrt, exp

a = 20
b = 0.2
c = 2*pi
n = 6
x = 3
individual = [1, 0, 3, 2, 4, 2]

def calculateAckley():
	sum1 = 0
	sum2 = 0

	for ind in individual:
		sum1 += ind**2
		sum2 += cos(c*ind)

	return -a*exp(-b*sqrt(sum1/n)) - exp(sum2/n) + a + 1
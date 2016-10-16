import math
from math import cos, sqrt, exp
from random import random, randrange, sample, gauss, seed

n = 30
min_v, max_v = -15.0, 15.0
# tenta mudar esses parametros
t1 = 3.0# 1.0/sqrt(2*n)
t2 = 3.0# 1.0/sqrt(2*sqrt(n))
min_step, max_step = 1e-8, 10
iterations = 100000

minimum_fitness = 1e20

def rand_in_range(x, y):
	return x + random()*(y-x)

def disturb_step(x, global_step):
	x *= exp(global_step + t2*gauss(0, 1))
	return min(max_step, max(min_step, x))

def disturb(x, s):
	x += s*gauss(0, 1)
	return min(max_v, max(min_v, x))

class Candidate:
	def __init__(self, value=None, step=None):
		if value is None:
			# Aleatory initialization
			self.value = [rand_in_range(min_v, max_v) for _ in range(n)]
			self.step = [rand_in_range(min_step, max_step) for _ in range(n)]
		else:
			# child of somebody
			self.value, self.step = value, step

		# fitness is always calculated, even when the candidate is created 
		self.calc_fitness()

	def calc_fitness(self):
		a, b, c = 20, 0.2, 2*math.pi
		sum1, sum2 = 0, 0
		for i in self.value:
			sum1 += i**2
			sum2 += cos(c*i)

		self.fitness = -a*exp(-b*sqrt(sum1/n)) - exp(sum2/n) + a + exp(1)

		global minimum_fitness
		if self.fitness < minimum_fitness:
			minimum_fitness = self.fitness

	def cross_alone(self):
		global_step = t1*gauss(0, 1)
		new_step = [disturb_step(x, global_step) for x in self.step]
		new_value = [disturb(self.value[i], new_step[i]) for i in range(n)]
		return Candidate(new_value, new_step)

def run_single_individual():
	seed()

	# executa mais vezes do que isso, pelo menos umas 30
	for _ in range(10):
		x = Candidate()

		for i in range(iterations):
			y = x.cross_alone()
			success = (y.fitness < x.fitness)
			if success:
				x = y

		print(x.fitness)

if __name__ == "__main__":
	run_single_individual()


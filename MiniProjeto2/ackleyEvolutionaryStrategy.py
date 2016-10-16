import math
from math import cos, sqrt, exp
from random import random, randrange, sample, gauss, seed

n = 30
t1 = 3.0#1.0/sqrt(2*n)
t2 = 1.0/sqrt(2*sqrt(n))
min_step, max_step = 1e-5, 10
min_v, max_v = -15.0, 15.0
iterations = 100000

minimum_fitness = 1e20

# 3. Usar também a recombinação feita por mhss no
# Mini-Projeto 1

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
			# 2 parents child
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

	def cross(self, other):
		new_v, new_s = [], []
		for i in range(n):
			new_v.append(rand_in_range(self.value[i], other.value[i]))
			new_s.append(rand_in_range(self.step[i], other.step[i]))

		return Candidate(new_v, new_s)

# 1+1
def run_single_individual():
	seed()
	print(t1, t2)

	for _ in range(10):
		x = Candidate()

		for i in range(iterations):
			y = x.cross_alone()
			success = (y.fitness < x.fitness)
			if success:
				x = y

		print(x.fitness)

# mi+lambda
population_size = 200
population = []
kids = []

def run_big_population():
	seed()
	global minimum_fitness
	minimum_fitness = 1e20

	# Aleatory initialization
	global population

	# Aleatory sample
	population = [Candidate() for i in range(population_size)]
	# 200 generations
	for i in range(2000):
		# 100 kids generated
		for j in range(100):
			recombination()
		survivorsSelection()
		print(i, "generation", minimum_fitness)

def recombination():
	'''
		2 aleatory parents and an aleatory cut
		The best out of the 2 children
	'''
	inds = sample(population, 2)
	
	child1, child2 = inds[0].cross(inds[1])

	if child1.fitness < child2.fitness:
		kids.append(child1)
	else:
		kids.append(child2)

def survivorsSelection():
	'''
		200 bests between the population and children 
	'''
	global population
	global kids

	wholeCrew = population + kids
	wholeCrew.sort(key=lambda x: x.fitness)
	population = wholeCrew[:population_size]
	kids = []

if __name__ == "__main__":
	run_single_individual()


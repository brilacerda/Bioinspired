import math
from math import cos, sqrt, exp
from random import random, randrange, sample, gauss, seed

n = 30
gauss_stddv = 0.45
minimum_fitness = 1e20

# 3. Usar também a recombinação feita por mhss no
# Mini-Projeto 1

def disturb(x):
	x += gauss(0, gauss_stddv)
	return min(15, max(-15, x))

class Candidate:
	def __init__(self, value=None):
		if value is None:
			# Aleatory initialization
			self.value = [random()*30.0 - 15.0 for _ in range(n)]
		else:
			# 2 parents child
			self.value = value

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
		return Candidate([disturb(x) for x in self.value])

	def cross(self, other):
		cut = randrange(1, n)
		new1 = self.value[:cut] + other.value[cut:]
		new2 = other.value[:cut] + self.value[cut:]

		# mutation
		if random() < 0.1:
			i = randrange(n)
			new1[i] = disturb(new1[i])
		if random() < 0.1:
			i = randrange(n)
			new2[i] = disturb(new2[i])

		return Candidate(new1), Candidate(new2)

# 1+1
def run_single_individual():
	seed()
	print(gauss_stddv)
	for _ in range(10):
		x = Candidate()

		# 200 generations
		for i in range(100000):
			y = x.cross_alone()
			if y.fitness < x.fitness:
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


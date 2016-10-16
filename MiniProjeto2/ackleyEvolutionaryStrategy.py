import math
from math import cos, sqrt, exp
from random import random, randrange, sample, gauss, seed

n = 30
_adjust = 0.99
_gauss_stddv = 6

gauss_stddv = _gauss_stddv
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

class LastRuns:
	def __init__(self):
		self.array = []
		self.success = 0

	def push(self, v):
		if v:
			self.success += 1
		self.array.append(v)

		if len(self.array) > 5:
			if self.array[0]:
				self.success -= 1
			self.array = self.array[1:]

	def percent_success(self):
		return float(self.success) / float(len(self.array))

def limit(x):
	return min(10, max(0.001, x))

# 1+1
def run_single_individual():
	seed()
	global gauss_stddv
	print(_gauss_stddv, _adjust)

	for _ in range(10):
		gauss_stddv = _gauss_stddv
		adjust = _adjust

		x = Candidate()
		last_runs = LastRuns()

		# 200 generations
		for i in range(100000):
			y = x.cross_alone()
			success = (y.fitness < x.fitness)
			if success:
				x = y

			last_runs.push(success)
			p_success = last_runs.percent_success()
			if p_success > 0.2:
				gauss_stddv = limit(gauss_stddv/adjust)
			elif p_success < 0.2:
				gauss_stddv = limit(gauss_stddv*adjust)

		print(gauss_stddv, x.fitness)

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


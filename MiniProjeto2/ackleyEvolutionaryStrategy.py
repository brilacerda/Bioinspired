import math
from math import cos, sqrt, exp
from random import random, randrange, sample, gauss, seed, shuffle

n = 30
min_v, max_v = -15.0, 15.0
# testa mudar esses parametros
t1 = 3.0# 1.0/sqrt(2*n)
t2 = 3.0# 1.0/sqrt(2*sqrt(n))
min_step, max_step = 1e-8, 10
population_size = 20
children_ratio = 7
generations = 500

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

	def walk(self):
		global_step = t1*gauss(0, 1)
		self.step = [disturb_step(x, global_step) for x in self.step]
		self.value = [disturb(self.value[i], self.step[i]) for i in range(n)]

		# recalculate fitness
		self.calc_fitness()

	# tenta mudar esse operador se quiser
	def cross(self, other):
		new_v, new_s = [], []
		for i in range(n):
			if randrange(2) == 0:
				new_v.append(self.value[i])
			else:
				new_v.append(other.value[i])
			new_s.append(rand_in_range(self.step[i], other.step[i]))

		return Candidate(new_v, new_s)

def new_generation(population):
	kids = []
	for _ in range(children_ratio*population_size):
		parents = sample(population, 2)
		child = parents[0].cross(parents[1])
		kids.append(child)
	return kids

def mario_breeding(pop):
	kids = []
	tot = len(pop)
	if tot <= 1:
		return kids

	q1, q2 = tot>>1, (tot+1)>>1
	half1, half2 = pop[q2:], pop[:q2]

	for _ in range(children_ratio):
		shuffle(half1)
		kids += [half1[i].cross(half2[i]) for i in range(q1)]

	return kids + mario_breeding(half2)

def selectSurvivors(population):
	population.sort(key=lambda x: x.fitness)
	return population[:population_size]

def run_big_population():
	seed()
	global minimum_fitness

	for _ in range(10):
		minimum_fitness = 1e20
		# Aleatory initialization
		population = [Candidate() for i in range(population_size)]

		# for every generation
		for i in range(generations):
			kids = mario_breeding(sorted(population, key=lambda x: x.fitness))
			# kids = new_generation(population)

			# updates every candidate with its ES parameters
			for x in population:
				x.walk()
			for x in kids:
				x.walk()

			population = selectSurvivors(population + kids)
			# population = selectSurvivors(kids)
			if i%100 == 0:
				print(population[0].fitness)

		print(minimum_fitness)

if __name__ == "__main__":
	run_big_population()


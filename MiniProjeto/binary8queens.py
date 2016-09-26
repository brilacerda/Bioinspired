from random import *

toBinary = {
	'0' : '000',
	'1' : '001',
	'2' : '010',
	'3' : '011',
	'4' : '100',
	'5' : '101',
	'6' : '110',
	'7' : '111'
}

# Criar a representação da estrutura ex.:
# [000, 001, 010, 011, 100, 101, 110, 111]
population_size = 100
population = {}
sample = ['000', '001', '010', '011', '100', '101', '110', '111']
fitness = []
worsts = []

def main():
	foundSolution = False
	# Inicialização aleatória
	# Geração de 100 indivíduos
	for i in range(population_size):
		shuffle(sample)

		# Avaliação da solução
		if checkSolution(sample, -1):
			print ("Solution ", sample, "found at iteration #", i, "when creating population")
			foundSolution = True
			break
		else:
			population[i] = sample;
			print ("ind #%s "%i)
			print (sample)
			print ("fitness ", fitness)

	if not foundSolution:
		for g in range(9900):
			print ("generation #", g)
			# every loop run, we check fitness twice
			g -= 2

			selectedParents = two_outta_five()
			children = [population[selectedParents[0]], population[selectedParents[1]]]

			# 90% chance to crossover
			crossChance = randrange(101)
			print ("crossover chance: ", crossChance)
			if crossChance < 10:
				print (crossChance, " crossover")
				children = crossover(selectedParents[0], selectedParents[1])

			# 40% chance to perform a mutation for each child
			if randrange(101) < 40:
				binMutation(children[0], randrange(3))
			if randrange(101) < 40:
				binMutation(children[1], randrange(3))
			
			# Get all the fitnesses & check solutions
			f1 = getFitness(children[0])
			if f1 == 0:
				print ("Solution ", children[0], "found at iteration #", g, " when checking children solution")
				break
			f2 = getFitness(children[1])
			if f2 == 0:
				print ("Solution ", children[1], "found at iteration #", g, "  when checking children solution")
				break

			# Selecting the individuals for the next generation
			if worsts == []:
				getTheWorsts()
			print ("worsts: " , worsts)
			population[worsts[0]] = f1
			worsts.pop(0)
			if worsts == []:
				getTheWorsts()
			print ("worsts: " , worsts)
			population[worsts[0]] = f2
			worsts.pop(0)

			# convertendo pra fenótipo
			# print int('00100001', 2)

# convertendo pra fenótipo
def getFenotype(ind):
    arr = []
    for i in range(8):
            arr.append(int(ind[i], 2))
    return arr

def hasDuplicatedColumn(ind):
	'''
		Transforms the individual into a set and see if there is any 
		repeated numbers, indicating the set to be smaller then 8.
	'''
	return (8 - len(set(ind)))

def hasMatchAtBottomToTopDiagonal(ind):
	'''
		Identify all diagonals from left to right, from the bottom to 
		the top by the sum of it. In the same diagonal the sum must 
		be the equal.
	'''
	indSum = []
	for i in range(8):
		indSum.append(i + ind[i])
	
	return (8 - len(set(indSum)))

def hasMatchAtToptoBottomDiagonal(ind):
	'''
		Identify all diagonals from left to right from the top to the 
		bottom by the reduction of the coordinates to the extremes -
		left and top - and comparing it.
		ex.: (1, 3) -> smaller number = 1; (1-1, 3-1) = (0, 2) extreme top.
		ex.: (5, 4) -> smaller number = 4; (5-4, 4-4) = (1, 0) extreme left.
	'''
	diag = []
	for i in range(8):
		# linha < coluna
		if ind[i] < i:
			diag.append((0, i - ind[i]))
		else:
			diag.append((ind[i] - i, 0))
	return (8 - len(set(diag)))

def getFitness(ind):
	'''
		The fitness end up being the number of colisions this time
	'''
	ind = getFenotype(ind)
	print(ind)
	colisions = hasDuplicatedColumn(ind) + hasMatchAtBottomToTopDiagonal(ind) + hasMatchAtToptoBottomDiagonal(ind)
	return colisions

def checkSolution(ind, i=0):
	'''
		The variable i is the position in the population array.
		If i == -1 it means we are checking the first generation, 
		so we need to populate the fitness first.
	'''
	colisions = getFitness(ind)
	if colisions == 0:
		return True
	else:
		if i == -1:
			fitness.append(colisions)
		else:
			fitness[i] = colisions
		return False

def two_outta_five():
	'''
		Catches the first 2 random individuals, give the best variable
		the index of the smaller fitness and the second best gets the
		second best'.
		Keep comparing the smaller fitness and return the 2 bests outta
		five random individuals.
	'''
	five_guys = []
	best = snd_best = population_size
	for i in range(5):
		five_guys.append(randrange(population_size))
		if i > 1:
			if fitness[five_guys[i]] < fitness[best]:
				snd_best = best
				best = five_guys[i]
			elif fitness[five_guys[i]] < fitness[snd_best]:
				snd_best = five_guys[i]
		elif i == 1:
			if fitness[five_guys[0]] < fitness[five_guys[1]]:
				best = five_guys[0]
				snd_best = five_guys[1]
			else:
				best = five_guys[1]
				snd_best = five_guys[0]
		
	# print (five_guys)
	return (best, snd_best)

def get_the_worst_fitness():
	worst = -1
	for i in range(population_size):
		if fitness[i] > worst:
			worst = fitness[i]
	return worst

def getTheWorsts():
	worstFit = get_the_worst_fitness()
	for i in range(population_size):
		if fitness[i] == worstFit:
			worsts.append(i)

def binMutation(ind, position):
	mut = randrange(8)
	element = ind[mut]
	mutation = ''
	for i in range(3):
		if i == position:
			if element[i] == '1':
				mutation += '0'
			else:
				mutation += '1'
		else:
			mutation += element[i]
	ind[mut] = mutation
	return ind

def mutation(ind):
	rand1 = randrange(8)
	rand2 = randrange(8)
	if rand1 == rand2:
		# try again
		return mutation(ind)
	else:
		temp = ind[rand1]
		ind[rand1] = ind[rand2]
		ind[rand2] = temp
		return ind

def crossover(ind1, ind2):
	children1 = []
	children2 = []
	cut = randrange(2)
	print (cut)
	for i in range(8):
		child1 = child2 = ''
		for x in range(3):
			if x <= cut:
				child1 += ind1[i][x]
				child2 += ind2[i][x]
		#		print (x," <= ",cut, " child1: ", child1," child2: ", child2)
			else:
				child1 += ind2[i][x]
				child2 += ind1[i][x]
		#		print (x," >  ",cut, " child1: ", child1," child2: ", child2)
		children1.append(child1)
		children2.append(child2)
	return [children1, children2]


# def individualToBinary(ind):
# 	temp = []
# 	for i in range(8):
# 		temp[i] = toBinary[str(ind[i])]
# 		print (temp[i])

# 	return temp
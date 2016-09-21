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
population_size = 10
population = {}
sample = ['000', '001', '010', '011', '100', '101', '110', '111']
fitness = []

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

def checkSolution(ind, i):
	'''
		If i == -1 it means we are checking the first generation, so we need 
		to populate the fitness first.
	'''

	ind = getFenotype(ind)
	print(ind)
	colisions = hasDuplicatedColumn(ind) + hasMatchAtBottomToTopDiagonal(ind) + hasMatchAtToptoBottomDiagonal(ind)
	if colisions == 0:
		return True
	else:
		if i == -1:
			fitness.append(colisions)
		else:
			fitness[i] = colisions
		return False

# def individualToBinary(ind):
# 	temp = []
# 	for i in range(8):
# 		temp[i] = toBinary[str(ind[i])]
# 		print (temp[i])

# 	return temp


# Inicialização aleatória
# Geração de 100 indivíduos
for i in range(population_size):
	shuffle(sample)

	# Avaliação da solução
	if checkSolution(sample, -1):
		print ("Solution %s found at iteration #%d" % sample, i)
		break
	else:
		population[i] = sample;
		print (sample)
		print ("fitness ", fitness)


# convertendo pra fenótipo
# print int('00100001', 2)

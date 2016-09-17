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
population = {}
sample = ['000', '001', '010', '011', '100', '101', '110', '111']
print (population)

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
	if len(set(ind)) < 8:
	 	return True
	else: 
		return False

def hasMatchAtBottomToTopDiagonal(ind):
	'''
		Identify all diagonals from left to right, from the bottom to 
		the top by the sum of it. In the same diagonal the sum must 
		be the equal.
	'''
	indSum = []
	for i in range(8):
		indSum.append(i + ind[i])
	
	if len(set(indSum)) < 8:
		return True
	else: 
	 	return False

def hasMatchAtToptoBottomDiagonal(ind):
	'''
		Identify all diagonals from left to right from the top to the 
		bottom by the reduction of the coordinates to the extremes -
		left and top - and comparing it.
	'''
	diag = []
	for i in range(8):
		# linha < coluna
		if ind[i] < i:
			diag.append((0, i - ind[i]))
		else:
			diag.append((ind[i] - i, 0))
	print (diag)
	if len(set(diag)) < 8:
		return True
	else: 
	 	return False		

def checkSolution(ind):
	ind = getFenotype(ind)
	if hasDuplicatedColumn(ind):
		return True
	elif hasMatchAtBottomToTopDiagonal(ind):
		return True
	elif hasMatchAtToptoBottomDiagonal(ind):
		return True
	else:
		return False

# def individualToBinary(ind):
# 	temp = []
# 	for i in range(8):
# 		temp[i] = toBinary[str(ind[i])]
# 		print (temp[i])

# 	return temp


# Inicialização aleatória
# Geração de 100 indivíduos
for i in range(10):
	shuffle(sample)

	# Avaliação da solução
	# if checkSolution(sample)
	# 	print ("Solution %s found at iteration #%d" % sample, i)
	# 	break

	population[i] = sample;
	print (sample)


# convertendo pra fenótipo
# print int('00100001', 2)

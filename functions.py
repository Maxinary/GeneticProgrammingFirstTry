from math import log

def checkfit(funclist):
	testcases = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]]
	fitness = []

	for i in len(funclist):
		fitness.append(0)
		for j in testcases:
			fitness[i] += abs(funclist[i](j[0]) - j[1])
	return fitness

def reap(funclist, fitlist):
	#cuts population in half
	pass

def mutate(funclist):
	#doubles population
	pass

def interpret_block(simple_lisp):
	'''interprets one branch of very simple lisp variation I made
		(+ m n) adds two items
			did not add in subtraction because it will more easily represented as adding a neg number
		(* m n) multiplies
		(/ m n) divides
			left division in because I want to work with integers for the time being
		(x m n) does m to the power of n
		(l m n) does log m base n

		will allow nesting later
	'''
	end_m = simple_lisp.find(" ",3)
	m = int(simple_lisp[3:end_m])
	n = int(simple_lisp[end_m + 1:-1])

	if simple_lisp[1]== '+':
		return m + n
	elif simple_lisp[1]== '*':
		return m * n		
	elif simple_lisp[1]== '/':
		return m / n
	elif simple_lisp[1]== 'x':
		return m ** n
	elif simple_lisp[1]== 'l':
		return log(m, n)
	else:
		return "Invalid Structure"

from math import log

def checkfit(funclist):
	testcases = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8],[9,9],[10,10],[11,11]]
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
	'''
	if simple_lisp.count("(") == simple_lisp.count(")"):
		
		end_m = get_end_of_block(simple_lisp[3:])
		m = simple_lisp[3:end_m+4]
		n = simple_lisp[end_m+5:-1]

		print(m,n)

		if m[0] == "(":
			m = interpret_block(m)
		if n[0] == "(":
			n = interpret_block(n)

		if simple_lisp[1] in ['+', '*', '/', '^', 'l']:
			m = float(m)
			n = float(n)
			if simple_lisp[1]== '+':
				return m + n
			elif simple_lisp[1]== '*':
				return m * n		
			elif simple_lisp[1]== '/':
				return m / n
			elif simple_lisp[1]== '^':
				return m ** n
			elif simple_lisp[1]== 'l':
				return log(m, n)
		else:
			return "Err:Operand"
	return "Err:Unbalanced Parentheses"

def get_end_of_block(simple_lisp):
	if simple_lisp[0] == "(":
		parenthesis = 0
		for i in range(len(simple_lisp)):
			if simple_lisp[i] == '(':
				parenthesis += 1
			if simple_lisp[i] == ')':
				parenthesis -= 1

			if parenthesis == 0:
				return i
	else:
		print("Tru")
		return simple_lisp.find(" ")-1

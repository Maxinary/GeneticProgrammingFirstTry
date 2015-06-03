from math import log

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
		return simple_lisp.find(" ")-1

if __name__ == "__main__":
	print(interpret_block(raw_input("> ")))

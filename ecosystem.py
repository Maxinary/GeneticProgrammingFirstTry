import lispish
import re
from random import randint, choice

def find_nth_char(haystack, needle, n):
	count = 0
	for i in range(len(haystack)):
		if haystack[i] == needle:
			count += 1
		if count == n:
			return i
	return -1

class Ecosystem():
	def __init__(self, population_exponential, testcases):
		self.population = [Organism("1")]
		self.testcases = testcases
		for i in range(population_exponential):
			self.mutate()
		self.testcases = testcases

	def mutate(self):
		print "Mutate"
		#mutates each of best, in duplicte
		''' 
		possible mutations:
			change operand
				(+ 1 2) -> (* 1 2)
			remove a branch
				(+ (* 2 3) 4) -> (+ 2 4)
			change number
				(+ 1 2) -> (+ 2 2)
			create new branch
				1 -> (+ 1 x)
		'''
		newpopulation = self.population
		looper = self.population
		for i in range(len(looper)):
			change = looper[i].lispish
			node_to_change = find_nth_char(change, "(", randint(0,change.count("(")))
			if node_to_change != -1 and change.count("(") >0:
				index = lispish.get_end_of_block(change[node_to_change:])
				block = change[node_to_change:index+node_to_change+1]

				end_m = lispish.get_end_of_block(block[3:])
				m = block[3:end_m+4]
				end_n = lispish.get_end_of_block(block[end_m+4:])
				n = block[end_m+3:end_m+3+end_n]

				decision = randint(0,2)

				if decision == 0:
					#changes operand
					newblock = block
					newblock = newblock[:1]+lispish.random_operand()+newblock[3:]
					change.replace(block,newblock)
				elif decision == 1:
					#removes branch
					chosen_one = randint(0,1)
					change = change.replace(block, [m,n][chosen_one], 1)
				elif decision == 2:
					change = self.create_branch(change,block)
				else:
					change = self.alter_num(change)
			else:
				decision = randint(0,1)
				if decision == 0:
					change = self.create_branch(change, change)
				else:
					change = self.alter_num(change)
			newpopulation.append(Organism(change))
		self.population = newpopulation

	def reap(self):
		#removes least fit half
		pass

	def update_fit(self):
		for i in self.population:
			self.population[i].fitness = 0
			for j in self.testcases:
				self.population[i].fitness += abs(funclist[i](j[0]) - j[1])

	def create_branch(self, full, inblock):
		#creates branch
		varia = randint(0,1)
		if varia == 0:
			full = full.replace(inblock,"("+lispish.random_operand()+" "+inblock+" "+str(randint(-5,5))+")",1)
		else:
			full = full.replace(inblock,"("+lispish.random_operand()+" "+inblock+" x)",1)
		return full

	def alter_num(self,full):
		#changes number
		nums = re.findall("-?\d+",full)
		chosen = choice(nums+["-123456"])
		new = str(int(chosen)+randint(-5,5))
		full = full.replace(chosen,new,1)
		full = re.sub("-+", "-", full)
		return full

class Organism():
	def __init__(self, lispish):
		self.lispish = lispish
		self.fitness = 0

if __name__ == "__main__":
	a = Ecosystem(0, [[1,1]])
	print [x.lispish for x in a.population]
	for k in range(0,5):
		print "\n\n"
		a.mutate()
		for x in a.population:
			print x.lispish
	while 1:
		

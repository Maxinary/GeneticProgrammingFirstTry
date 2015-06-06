import lispish
import re
from random import randint, choice
from sys import exit
from os import environ
try:
	if environ["DISPLAY"] is not None:
		from matplotlib.pyplot import plot,show
		import numpy as np
except KeyError:
	pass
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
		self.iterations = 0
		self.win = None
		for i in range(population_exponential):
			self.mutate()


	def mutate(self):
		self.iterations += 1
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
				n = block[end_m+5:-1]

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
		self.update_fit()
		errors = 0
		newpop = self.population
		for i in newpop:
			if i.fitness == "e":
				try:
					self.population.remove(i)
					errors += 1
				except ValueError:
					pass

		self.population.sort(key=lambda x: x.fitness, reverse=True)
		for i in range(len(self.population) - (len(self.population) + errors)/2):
			self.population.remove(self.population[i])

	def update_fit(self):
		for i in range(len(self.population)):
			self.population[i].fitness = 0
			try:
				for j in self.testcases:
					self.population[i].fitness += abs(lispish.interpret_block(self.population[i].lispish, {"x":j[0]}) - j[1])


				if self.win == None:
					self.win = self.population[i]

				elif self.population[i].fitness <= self.win.fitness:
					if len(self.population[i].lispish) < len(self.win.lispish):
						self.win = self.population[i]
					if self.population[i].fitness < self.win.fitness:
						self.win = self.population[i]

			except Exception, e:
				self.population[i].fitness = "e"

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
		chosen = choice(nums+["0"])
		new = str(int(chosen)+randint(-5,5))
		full = full.replace(chosen,new,1)
		full = re.sub("-+", "-", full)
		return full

class Organism():
	def __init__(self, lispish):
		self.lispish = lispish
		self.fitness = 0

if __name__ == "__main__":
	a = Ecosystem(6, [[x,(x-2)**2] for x in range(0,10)])
	try:
		while 1:
			a.reap()
			a.mutate()
			print "Winning:",a.win.lispish
			print "Fitness:",a.win.fitness
			print "Iterations:",a.iterations
	except KeyboardInterrupt:
		try:
			xvals = [x[0] for x in a.testcases]
			yvals = [x[1] for x in a.testcases]
			plot(xvals, [lispish.interpret_block(a.win.lispish, {"x":i}) for i in xvals], 'b', xvals, yvals, "g^")
			show()
		except Exception, e:
			print "\nCould not display graph"

class Ecosystem():
	def __init__(self, population_exponential, testcases):
		self.population = [Organism()]
		self.testcases = 
		for i in xrange(population_exponential):
			self.mutate(self.population)
		self.testcases = testcases

	def mutate():
		#mutates each of best, in duplicte
		pass

	def reap():
		#removes least fit half
		pass

	def update_fit():
		for i in self.population:
			self.population[i].fitness = 0
			for j in self.testcases:
				self.population[i].fitness += abs(funclist[i](j[0]) - j[1])
class Organism():
	def __init__(self):
		self.lispish = "(+ 1 1)"
		self.fitness = 0

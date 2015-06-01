import regs
testcases = [[0,0],[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]]
fitness = []

for i in len(regs.list):
	for j in testcases:
		fitness[i] += abs(regs.list[i](j[0]) - j[1])

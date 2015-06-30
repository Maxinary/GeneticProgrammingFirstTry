from ecosystem import *
from json import loads, dumps
from time import time
from os import system
from hashlib import sha1

cf = open("cross.out","r+")
mf = open("mutate.out","r+")

def run(cross, minute_len, points):
	filename = sha1(str(points)+str(minute_len)).hexdigest()
	system("touch "+filename)
	out_file = open(filename, "r+")
	a = Ecosystem(3, points)
	answer = None
	
	try:
		current = loads(out_file.read())
		print current["points"]
		print current["time"]
		print current["runs"]
	except ValueError, KeyError:
		current = current = {"points":points,"time":minute_len, "runs":[]}
	if not isinstance(current, dict):
		current = {"points":points,"time":minute_len, "runs":[]}
	
	print current
	log = []
	start_t = time()
	end_t = time()+60*minute_len
	while time() < end_t:
		a.reap()
		a.mutate()
		a.cross()
		a.reap()
		if a.win != answer:
			log.append([a.win.fitness, a.iterations, time()-start_t])
			print log[-1]
			answer = a.win
	log.append([a.win.fitness, a.iterations, time()-start_t])
	current["runs"].append(log)
	print "End", current
	out_file.seek(0)
	out_file.write( dumps(current) )
	out_file.truncate()
	out_file.close()

for i in range(5):
	run(True, .05, [[x,(x+3)**3 - 9*x] for x in range(1,10)])

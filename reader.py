from Tkinter import Tk
from tkFileDialog import askopenfilename
import matplotlib.pyplot as plt
from json import loads

data = ["fitness", "iterations", "time"]

def read(xaxis,yaxis):
	Tk().withdraw()
	filename = askopenfilename()
	f = open(filename, "r")
	try:
		loaded_file = loads(f.read())
		print loaded_file["points"]
		print loaded_file["time"]
		print loaded_file["runs"]
	except ValueError, KeyError:
		f.close()
		return "Error, file corrupted"
	indeces = []
	for j in [xaxis,yaxis]:
		if j in data:
			indeces.append(data.index(j))
		else:
			f.close()
			return "Invalid axis"
	loaded_file
	for i in loaded_file["runs"]:
		plt.plot([x[indeces[0]] for x in i],[x[indeces[1]] for x in i])
	plt.show()
	return ""
	
read("time","iterations")

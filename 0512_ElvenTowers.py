import numpy as np
import csv
import pandas as pd
import re
#opens a file dialog in the current folder (detailed)
from tkinter import filedialog as fd
filename = fd.askopenfilename()
inputtxt=open(filename,'r')
data={1:['[T]','[V]','[J]','[W]','[N]','[R]','[M]','[S]'],
2:['[V]','[C]','[P]','[Q]','[J]','[D]','[W]','[B]'],
3:['[P]','[R]','[D]','[H]','[F]','[J]','[B]'],
4:['[D]','[N]','[M]','[B]','[P]','[R]','[F]'],
5:['[B]','[T]','[P]','[R]','[V]','[H]'],
6:['[T]','[P]','[B]','[C]'],
7:['[L]','[P]','[R]','[J]','[B]'],
8:['[W]','[B]','[Z]','[T]','[L]','[S]','[C]','[N]'],
9:['[G]','[S]','[L]']}
for keys in data.keys():
	data[keys]=list(reversed(data[keys]))
# elfTower=pd.DataFrame(data)

def towermove(filename=inputtxt,tower=data):
	for line in filename.readlines():
		if line.startswith('move'):
			ints=[int(x) for x in re.findall(r'\d+',line)]
			print(">>>>", tower)
			print(ints)
			# movingboxes=list(reversed(tower[ints[1]][-ints[0]:]))
			movingboxes=tower[ints[1]][-ints[0]:]
			tower[ints[2]].extend(movingboxes)
			tower[ints[1]]=tower[ints[1]][:-ints[0]]
			print(tower)

	return(tower)
towers=towermove(inputtxt,data)
lasted=[]
for keys in towers.keys():
	last=towers[keys]
	print(keys,last)
	lasted.append(last[-1])
print(lasted)



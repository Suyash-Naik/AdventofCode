import numpy as np
#opens a file dialog in the current folder (detailed)
from tkinter import filedialog as fd
filename = fd.askopenfilename() #select the input file from Advent
cleanList=open(filename,'r')
pairList=cleanList.readlines()
commons=0
intersects=0
for line in pairList:
	commaindex=line.find(",")
	# print(line[:commaindex],line[commaindex+1:])
	dashindex1=line[:commaindex].find("-")
	dashindex2=line[commaindex+1:].find("-")
	elfgroup1=list(range(int(line[:commaindex][:dashindex1]),int(line[:commaindex][dashindex1+1:])+1))
	elfgroup2=list(range(int(line[commaindex+1:][:dashindex2]),int(line[commaindex+1:][dashindex2+1:])+1))
	if set(elfgroup1).issubset(set(elfgroup2)) or set(elfgroup2).issubset(set(elfgroup1)):
		commons+=1
	if set(elfgroup1) & set(elfgroup2):
		intersects+=1
print(commons,intersects)

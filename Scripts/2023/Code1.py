import pandas as pd
#opens a file dialog in the current folder (detailed)
from tkinter import filedialog as fd
filename = fd.askopenfilename() #select the input file from Advent
#opens the file and then reads the lines
food=open(filename,'r')
lineFood= food.readlines()
#data saving? may not be the most efficient
dataframe={} #database with {elf:cal}
elfNum=1 #index of the elf
cal=0 #number of calories on the given elf
for line in lineFood:
	if line!="\n":
		cal=cal+int(line)
	elif line=="\n":
		dataframe[elfNum]=[cal]
		cal=0
		elfNum+=1
#dataframe magic
pdDataframe=pd.DataFrame(dataframe)
callist=pdDataframe.values[0]
callist=sorted(callist,reverse=True)
#basic ouputting
print('first prob:')
print(callist[0])
print('second prob:')
print(callist[0]+callist[1]+callist[2])
#The end :D first advent code!

import pandas as pd

food=open("/home/snaik/Documents/AdevntofCode2022/input",'r')
lineFood= food.readlines()

dataframe={}
elfNum=1
cal=0
for line in lineFood:
	if line!="\n":
		cal=cal+int(line)
	elif line=="\n":
		dataframe[elfNum]=[cal]
		cal=0
		elfNum+=1

pdDataframe=pd.DataFrame(dataframe)
callist=pdDataframe.values[0]
callist=sorted(callist,reverse=True)
print('first prob:')
print(callist[0])
print('second prob:')
print(callist[0]+callist[1]+callist[2])

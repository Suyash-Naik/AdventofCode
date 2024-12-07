import numpy as np
#opens a file dialog in the current folder (detailed)
from tkinter import filedialog as fd
# filename = fd.askopenfilename() #select the input file from Advent
# print(filename)
filename='/home/snaik/Documents/AdventofCode2022/input_0612.txt'
testtxt="nppdvjthqldpwncqszvftbrmjlhg"
# Open the text file containing the letters
with open(filename) as f:
    # Read the contents of the file as a string
    letters = f.read()

# Convert the string to a numpy array
letters_array = np.array([letter for letter in letters])
# letters_array=np.array([letter for letter in testtxt])
print(letters_array)
# Print the numpy array
letters_array = letters_array[:-1]
def isunique(comparearray=letters_array):
	for i in range(len(comparearray)):
		if i>=3:
			signalcode=[x for x in comparearray[i-3:i+1]]
			setcode=set(signalcode)
			if len(setcode)==4:
				print(i+1,setcode)
				break
isunique(letters_array)
def new14marker(comparearray=letters_array):
	for i in range(len(comparearray)):
		if i>=13:
			signalcode=[x for x in comparearray[i-13:i+1]]
			setcode=set(signalcode)
			if len(setcode)==14:
				print(i+1,setcode)
				break
new14marker(letters_array)


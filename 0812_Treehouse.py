'''make a class called Treehouse that can read a txt file with a matrix of numbers and see if the position of a select number is smaller
atleast one other number in the matrix in its row and column. alse. 
'''
import numpy as np
#opens a file dialog in the current folder (detailed)
from tkinter import filedialog as fd
filename = fd.askopenfilename() #select the input file from Advent
print(filename)

# define a class called Treehouse a method in which is to read the txt file and maintain the matrix of numbers
data = open(filename).readlines()
matrix=[list(map(int, line[:-1])) for line in data]
matrix=np.array(matrix)
#define a function that checks the number of elements in the matrix which are larger than the rest of the elements in their row and column
martix2=np.array([[3,0,3,7,3],
[2,5,5,1,2],
[6,5,3,3,2],
[3,3,5,4,9],
[3,5,3,9,0]])
def find_visible(matrix):
    visible = 0
    nR,nC=matrix.shape
    hidden = np.ones(matrix.shape)
    #visible = nR+nC
    #check visibility from left to right
    for i in range(nR):
        for j in range(nC):
            if i==0 or i==nR-1 or j ==0 or j==nC-1:
                visible+=1
                hidden[i,j]=0
            else:
                if (
                np.all(matrix[i, j] > matrix[i, :j])  # Compare with elements to the left
                or np.all(matrix[i, j] > matrix[i, j+1:])  # Compare with elements to the right
                or np.all(matrix[i, j] > matrix[:i, j])  # Compare with elements above
                or np.all(matrix[i, j] > matrix[i+1:, j])  # Compare with elements below
            ):
                    visible+=1
                    hidden[i,j]=0

                   
    return (visible)

print(f"Part 1: The number of visible trees are {find_visible(matrix)}")

#Part 2
def TreeCount(value,matrix):
    count=0
    for tree in matrix:
        count+=1
        if tree>=value:
            return count
    return count
        
def find_Scenic(matrix):
    scenic=np.empty(matrix.shape)
    nR,nC=matrix.shape
    for i in range(nR):
        for j in range(nC):
            l=TreeCount(matrix[i,j],np.flip(matrix[i,:j]))
            r=TreeCount(matrix[i,j],matrix[i,j+1:])
            u=TreeCount(matrix[i,j],np.flip(matrix[:i,j]))
            d=TreeCount(matrix[i,j],matrix[i+1:,j])
            score=l*r*u*d
            scenic[i,j]=score
    return(scenic)
print(f'Part 2 {np.max(find_Scenic(matrix))})

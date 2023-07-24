import numpy as np
#opens a file dialog in the current folder (detailed)
from tkinter import filedialog as fd
filename = fd.askopenfilename() #select the input file from Advent
print(filename)
filename='/Users/snaik/Documents/Coding/AOC/AdventofCode2022/Day09/input_0912'
rope=np.zeros([6,5])
posHead=[5,1]
posTail=[4,0]
tailloc=set([4,0])
moveMat={"U":[0,-1],"D":[0,1],"L":[-1,0],"R":[1,0]}

def checkHead(posHead,posTail,rope):
    row_h, col_h = posHead
    row_t, col_t = posTail

    # Check if PosTail is adjacent to PosHead in any direction
    if (row_t == row_h and abs(col_t - col_h) == 1) or (col_t == col_h and abs(row_t - row_h) == 1):
        return True

    return False
def moveHead(posHead,rope,move):
    if move[0]=='R':
        posHead[0]=(posHead[0]+int(move[2]))%6
    elif move[0]=='L':
        posHead[0]=(posHead[0]-int(move[2]))%6
    elif move[0]=='U':
        posHead[1]=(posHead[1]-int(move[2]))%5
    elif move[0]=='D':
        posHead[1]=(posHead[1]+int(move[2]))%5
    if not checkHead(posHead,posTail,rope):
        print('Head and Tail are not adjacent')
        #moveTail(posTail,rope,move)
    return posHead

def moveTail(posTail,posHead,rope,move,tailMat):    
    pass

for i,line in enumerate(open(filename).readlines()):
    if i<10:
        print(checkHead(posHead,posTail,rope))

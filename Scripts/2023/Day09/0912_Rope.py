import numpy as np
#opens a file dialog in the current folder (detailed)
from tkinter import filedialog as fd
#filename = fd.askopenfilename() #select the input file from Advent
#print(filename)
filename='/Users/snaik/Documents/Coding/AOC/AdventofCode2022/Day09/input_0912'
rope=np.zeros([6,5])
posHead=[5,0]
posTail=[5,0]
headMat=np.zeros([6,5])
headMat[posHead[0],posHead[1]]=1
print(headMat)
tailloc=set([4,0])
moveMat={"L":[0,-1],"R":[0,1],"U":[-1,0],"D":[1,0]}
def ecludianDist(posHead,posTail):
    return np.sqrt((posHead[0]-posTail[0])**2+(posHead[1]-posTail[1])**2)
 
def checkHead(posHead,posTail):
    
    # Check if PosTail is adjacent to PosHead in any direction
    if ecludianDist(posHead,posTail)<2:
        return True

    return False


def headMove(posHead,rope,move):
    movement=moveMat[move[0]]
    print('Movement to be done is {}:{} for {} times'.format(move[0],movement,move[2]))
    for i in range(int(move[2])):
        posHead[0]=(posHead[0]+movement[0])%6
        posHead[1]=(posHead[1]+movement[1])%5
        headMat=np.zeros([6,5])
        headMat[posHead[0],posHead[1]]=1
        print('Head is at {}'.format(posHead))
        print(headMat)
        if not checkHead(posHead,posTail):
            print('Head and Tail are not adjacent. Head is at {}. Tail is at {}'.format(posHead,posTail))
            #moveTail(posTail,rope,move)
    return posHead

def moveTail(posTail,posHead,rope,move,tailMat):    
    if not checkHead(posHead, posTail):
        if abs(posHead[0]-posTail[0])>abs(posHead[1]-posTail[1]):
            if posHead[0]>posTail[0]:
                movement=[1,0]
            else:
                movement=[-1,0]
        pass

for i,line in enumerate(open(filename).readlines()):
    if i<10:
        print(line)
        print(headMove(posHead,rope ,line))

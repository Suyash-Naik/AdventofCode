import numpy as np
import os
from glob import glob
import pandas as pd
from tkinter import filedialog as fd

IF=fd.askopenfilename()
matIF=np.loadtxt(IF)
print(f"Input File is stored in: {IF}")
print("____Solution1_________")
c1=matIF[:,0]
c1.sort()
c2=matIF[:,1]
c2.sort()
c3=np.abs(c1-c2)
print(f"Total distance between places is: {c3.sum()}")
print("____Solution2_________")
ue,counts=np.unique(c2,return_counts=True)
c2dict=dict(zip(ue,counts))
ue,counts=np.unique(c1,return_counts=True)
c1dict=dict(zip(ue,counts))
simlist=[]
for i in c1dict.keys():
    if i in c2dict.keys():
        simscore=i*c2dict[i]
        simlist.append(simscore)
print(f"The similarity score is: {np.sum(simlist)}")
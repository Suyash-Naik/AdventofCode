import sys
import re

def multi(num1:int,num2:int)->int:
    return num1*num2

def readstring(line:str,part:str)->int:
    """This reads a string and returns the sum of the multi of good characters"""
    
    pattern=r"mul\((\d+),(\d+)\)"
    pattern2=r"don't\(\)"
    pattern3=r"do\(\)"
    part2=0
    if part==1:
        functions=re.findall(pattern,line)
        return sum(multi(int(x[0]),int(x[1])) for x in functions)
    else:
        newstring=line
        for x in re.findall(pattern2,line):
            match2=re.search(pattern2,line)
            newstring=line[:match2.start()]
            # Update the lines to start from the first next occurrence of pattern3
            partline = lines[match2.end():]
            match3 = re.search(pattern3, partline)
            if not match3:
                break
            functions=re.findall(pattern,newstring)
            part2+=sum(multi(int(x[0]),int(x[1])) for x in functions)
            print(part2)
            lines = partline[match3.start():]
with open(sys.argv[1],"r") as f:
    lines=f.read()

print(f"part1 answer should be {readstring(lines,1)}")
print(f"part2 answer should be {readstring(lines,2)}")

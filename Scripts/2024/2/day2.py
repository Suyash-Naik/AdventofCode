def checker(nums:list)->bool:
    """This checks if a line is safe
    safe increaseing or decreasing not switching
    increase/decrease <4
    """
    if len(nums)<2:
        return False
    
    listdiff=[x1-x2 for x1,x2 in zip(nums,nums[1:])]
    firstsign= listdiff[0]>=0
    if not all(1<=abs(d)<=3 for d in listdiff):
        return False
    if not all((x>=0)==firstsign for x in listdiff):
        return False
    return True
def report_strict(line:str)->bool:
    level=[int(i) for i in line.split(" ")]
    return checker(level)

def report_allowance(line:str)->bool:
    level=[int(i) for i in line.split(" ")]
    if checker(level):
        return True
    for i in range(len(level)):
        if checker(level[:i]+level[i+1:]):
            return True
    return False
with open('/Users/snaik/Documents/AdventofCode/Data/2024/2/input.txt',"r") as f:
    lines=f.readlines()
    
safereps=[line for line in lines if report_strict(line)]
saferreps=[line for line in lines if report_allowance(line)]
print(f"There are {len(safereps)} safe reports if strict rules are applied")
print(f"There are {len(saferreps)} safe reports if allowance rules are applied")

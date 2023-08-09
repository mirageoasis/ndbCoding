import re
# (100+1+ | 01)+

# 10 (0)(1) or 01 

NO="NO"
YES="YES"

def cal(string : str):
    t=re.compile('(100+1+|01)+')
    if t.fullmatch(string):
        return "YES"
    else:
        return "NO"
    

N=int(input())

for i in range(N):
    string = input()
    print(cal(string))
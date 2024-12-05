import sys
from collections import defaultdict

n=int(input())

wrong_dict=defaultdict(int)

correct_set=set()

# 사람 이름
# 맞은 

for i in range(n):
    num, user_id, res, _, __, ___, ____ = sys.stdin.readline().split()

    if user_id == "megalusion":
        continue

    user_id=user_id
    res=int(res)

    if res != 4:
        if user_id not in correct_set:
            wrong_dict[user_id]+=1
    else:
        correct_set.add(user_id)



if not correct_set:
    print(0)
else:
    t=0
    for c in correct_set:
        t+=wrong_dict[c]
    
    print(len(correct_set) / (len(correct_set) + t) * 100)
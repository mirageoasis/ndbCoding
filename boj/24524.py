from bisect import bisect_left, bisect_right
from collections import defaultdict

S=input()
T=input()

l = [0 for _ in T]

idx_dict = dict()
for idx, i in enumerate(T):
    idx_dict[i] = idx

for i in S:
    if i in idx_dict:
        if idx_dict[i] == 0:
            l[0] += 1
        else:
            if l[idx_dict[i] - 1] > 0:
                l[idx_dict[i]] += 1
                l[idx_dict[i] - 1] -= 1

print(l[-1])

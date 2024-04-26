from math import sqrt, ceil

N = int(input())

LIM = ceil(sqrt(10000000)) + 1

li = [True for _ in range(LIM)]

li[0] = False
li[1] = False

for i in range(2, LIM):
    if li[i]:
        for j in range(i * 2, LIM, i):
            li[j] = False


    
for idx, i in enumerate(li[2:], start=2):
    if not i:
        continue
    if N == 1:
        break
    if N % idx == 0:
        while not (N % idx):
            print(idx)
            N //= idx

if N != 1:
    print(N)
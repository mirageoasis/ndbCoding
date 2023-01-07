import sys

N = int(input())

li = []

for i in range(N):
    name, score = sys.stdin.readline().rstrip().split()
    score = int(score)
    li.append((name, score))

li.sort(key = lambda x : x[1])

for name, score in li:
    print(name)
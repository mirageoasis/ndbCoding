N = int(input())

li = []

for i in range(N):
    t = input().split(' ')
    li.append([t[0], int(t[1]) , int(t[2]) , int(t[3])])

li.sort(key=lambda x : (-x[3], -x[2], -x[1]))

print(li[0][0])
print(li[-1][0])
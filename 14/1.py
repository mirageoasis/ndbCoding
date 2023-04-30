N=int(input())

li = []

for i in range(N):
    k = input().split()
    t = [k[0], int(k[1]), int(k[2]), int(k[3])]
    
    li.append(t)

#print(li)

li.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for l in li:
    print(l[0])
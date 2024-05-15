N=int(input())

li = []

for i in range(N):
    a ,b = map(int, input().split())
    li.append(b-a)

li.sort()

if len(li) % 2 == 0:
    print(li[len(li) // 2] - li[len(li) // 2 - 1] + 1)
else:
    print(1)
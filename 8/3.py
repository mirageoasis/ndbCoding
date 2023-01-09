N=int(input())
li=[0] * (N + 1)

li[1] = 1
li[2] = 3

for i in range(3, N+1):
    li[i] = (li[i - 1] + li[i - 2] * 2) % 796796

print(li[N])
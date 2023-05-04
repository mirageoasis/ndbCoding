N = int(input())

li = []

for i in range(N):
    temp =list(map(int ,input().split()))
    temp.insert(0, 0)
    temp.append(0)
    li.append(temp)

# row -1 -1 / -1 0

for i in range(1, N):
    for j in range(1, i + 2):
        li[i][j] += max(li[i - 1][j - 1], li[i - 1][j])

print(max(li[N-1]))
import sys

N=int(input())

li = []
LIM=200000000
# 10 ^ 3 ^ 4
# 일단 k 고르는 경우 N
# xyz 고르는 경우 N ^ 3
# 그리고 N ^ 2면 ㄱㅊ지 않음?

# 2개 선택해서 빼주고 뺀 값 index를 어캐 new_set에다 넣으면 안되나? 사전을 쓰자

d_d = dict()

for i in range(N):
    li.append(int(sys.stdin.readline()))

# i가 먼저 오는 수
for i in range(N):
    for j in range(N):
        key = li[i] - li[j]
        if key <= 0:
            continue
        if key not in d_d:
            d_d[key] = li[i]
        else:
            d_d[key] = max(d_d[key], li[i])

ans=-1
for i in range(N):
    for j in range(N):
        key = li[i] + li[j]
        if key in d_d:
            ans=max(ans, d_d[key])

print(ans)
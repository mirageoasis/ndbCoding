# 52
import sys

N, M, K = map(int, input().split())

closed=set()
parent=[i for i in range(N+1)]

stones=list(map(int, sys.stdin.readline().split()))

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    closed.add((min(a, b), max(a, b)))

# 다 연결된 케이스

# disjoint set, 각 집단마다 최소 돌 다리를 계산한다.
# 여기서 문제는 5번과 1번이 연결된다는 점이다. 그러면 양옆으로 이동하면서 최소값을 찾는다.
# 1번은 안하고 2번 부터 끝까지 탐색, 그리고 5번은 별도로 1번과 이어져있는지 탐색
# 왼쪽 차트, 오른쪽 차트 -> 부모가 최소인 경우만 남긴다. 2백만
# left, right parent 초기 설정
# left, right 둘다 재귀적으로 parent 설정하기
# 이후 left랑 rigth 중에서 작은 수를 parent로 삼는다.


def parent_find(parent, x):
    if parent[x] != x:
        parent[x] = parent_find(parent, parent[x])
    return parent[x]

def union_small(big, small, parent):
    big_parent=parent_find(parent, big)
    small_parent=parent_find(parent, small)

    if big_parent < small_parent:
        parent[small]=big_parent
    else:
        parent[big]=small_parent

for i in range(1, N):
    if (i, i+1) not in closed:
        union_small(i, i+1, parent)

# N번이 1번과 이어져있다면
if (1, N) not in closed:
    for idx, p in enumerate(parent):
        if p == parent[N]:
            parent[idx]=1

#print(parent)

INF=1_000_001
mini_stone=dict()

for p in parent:
    if p != 0:
        mini_stone[p]=INF

for idx, val in enumerate(parent):
    if idx != 0:
        mini_stone[val]=min(mini_stone[val], stones[idx-1])

val=sum(mini_stone.values())
# print(mini_stone)
# print(val)
if val > K and len(mini_stone) > 1:
    print("NO")
else:
    print("YES")
import sys
from collections import defaultdict
input=sys.stdin.readline

n, k = map(int, input().split())
friend=[]
for _ in range(n):
    friend.append(input().strip())

# 첫번째로 시작하고
# 첫번째를 dictionary로 만든다.
friend=[len(i) for i in friend]
window=defaultdict(int)
ans=0

for i in range(k+1):
    window[friend[i]]+=1
for _, v in window.items():
    if v != 0:
        ans+=v*(v-1)//2
#print(ans, window)
# 현재 계산하고 마지막에 결산을 한다.

for idx in range(k+1, n):
    # 제거 목록
    # idx - k - 1
    # 추가 목록
    # idx
    remove_elem=friend[idx-k-1]
    add_elem=friend[idx]
    #print(remove_elem, add_elem)
    window[remove_elem]-=1
    ans+=window[add_elem]
    window[add_elem]+=1
    #print(window)

print(ans)
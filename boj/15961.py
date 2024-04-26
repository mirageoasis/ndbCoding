# combination하면 안된다.

import sys
from collections import defaultdict

N, d, k, c = map(int, input().split())
# 길이, 총 개수, 연속, 쿠폰 번호
li = []
visit = [0 for i in range(d+1)]

for i in range(N):
    li.append(int(sys.stdin.readline()))

visit[c]=1
ans=1
#print(visit)

for i in li[:k]:
    if visit[i] == 0:
        ans+=1
    visit[i]+=1
temp_ans=ans
#print(temp_ans)
for i in range(1, N):
    # i 빼고
    # (i - 1) % N 제거 (i + k) % N 더하기
    first = li[i-1]
    last = li[(i+k-1) % N]
    visit[first]-=1
    visit[last]+=1
    #print(first, last)
    if visit[first] == 0:
        temp_ans-=1
    
    if visit[last] == 1:
        if last != c and last != first:
            temp_ans+=1
    #print(i, temp_ans)
    ans = max(temp_ans, ans)

print(ans)
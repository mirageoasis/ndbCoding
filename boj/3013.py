#10만 * 10만은 안된다.
# 수가 한번씩만 등장하는게 힌트인 듯


n, m = map(int, input().split())
li=list(map(int, input().split()))
# 위치 파악

idx=li.index(m)

# first_li
left_li=li[:idx][::-1]
right_li=li[idx+1:]

#print(left_li)
#print(right_li)
from collections import defaultdict
num=0
left_odd=defaultdict(int)
left_even=defaultdict(int)
for i in range(len(left_li)):
    if left_li[i] > m:
        num+=1
    else:
        num-=1
    if i % 2 == 0:
        left_odd[num]+=1
    else:
        left_even[num]+=1

num=0
right_odd=defaultdict(int)
right_even=defaultdict(int)
for i in range(len(right_li)):
    if right_li[i] > m:
        num+=1
    else:
        num-=1
    if i % 2 == 0:
        right_odd[num]+=1
    else:
        right_even[num]+=1

right_even[0]+=1
left_even[0]+=1
#print(right_even, right_odd)
#print(left_even, left_odd)
ans=0
for k, v in right_even.items():
    res=left_even[-k]
    ans+=res*v

for k, v in right_odd.items():
    res=left_odd[-k]
    ans+=res*v

print(ans)
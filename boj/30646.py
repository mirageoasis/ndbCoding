# 숫자 20만개

left_idx=dict()
right_idx=dict()

n=int(input())
li=list(map(int, input().split()))

for i in range(len(li)):
    if left_idx.get(li[i]) is None:
        left_idx[li[i]]=i
for i in range(len(li)-1, -1, -1):
    if right_idx.get(li[i]) is None:
        right_idx[li[i]]=i

prefix_sum=[0 for i in range(n+1)]
# [0 i) 까지의 합

for i in range(1, n+1):
    prefix_sum[i]+=prefix_sum[i-1]+li[i-1]

# max 값을 구하기
maxi=-1
#print(left_idx)
#print(right_idx)
for i in left_idx:
    maxi=max(maxi, prefix_sum[right_idx[i] + 1] - prefix_sum[left_idx[i]])
cnt=0
for i in left_idx:
    if maxi == prefix_sum[right_idx[i] + 1] - prefix_sum[left_idx[i]]:
        cnt+=1

print(maxi, cnt)
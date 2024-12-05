from bisect import bisect_left

# 59분 시작

n=int(input())
li=list(map(int, input().split()))

minus=[i for i in li if i < 0]
plus=[i for i in li if i >= 0]

minus.sort()
plus.sort()

ans=()

plus_ans=(10000000011, 10000000011)
minus_ans=(10000000011, 10000000011)

# plus로만 이뤄진거
if len(plus) >= 2:
    plus_ans=(plus[0], plus[1])

#minus로만 이뤄진거
if len(minus) >= 2:
    minus_ans=(minus[-2], minus[-1])

# total ans
total_ans=(10000000011, 10000000011)
for minu in minus:
    plus_idx=bisect_left(plus, -minu)

    if plus_idx < len(plus):
        plus_val=plus[plus_idx]
        if abs(sum(total_ans)) > abs(plus_val + minu):
            total_ans=(minu, plus_val)
    
    if plus_idx > 0:
        plus_val=plus[plus_idx-1]
        if abs(sum(total_ans)) > abs(plus_val + minu):
            total_ans=(minu, plus_val)

if abs(sum(plus_ans)) < abs(sum(total_ans)):
    total_ans=plus_ans

if abs(sum(minus_ans)) < abs(sum(total_ans)):
    total_ans=minus_ans

print(total_ans[0], total_ans[1])
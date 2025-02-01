# 큰거끼리 곱하면 좋음
# 만약에 0 있으면 음수와 묶는다.
# 양수는 끼리 묶는다.
# 0은 방치
# 음수는 0이랑 곱하든가 아니면 더하든가

n=int(input())
li=[]
for i in range(n):
    li.append(int(input()))
plus=[i for i in li if i > 0]
minus=[i for i in li if i < 0]
zero=[0 for i in li if i == 0]

# 작은거 앞에
plus.sort(reverse=True)
minus.sort()
zero.sort()
ans=0
#print(plus, minus, zero)
for i in range(0, len(plus), 2):
    if i == len(plus) - 1:
        ans+=plus[i]
    else:
        if plus[i] != 1 and plus[i+1] != 1:
            ans+=(plus[i] * plus[i+1])
        else:
            ans+=(plus[i] + plus[i+1])
#print(ans)
# 0을 없에야 한다.
# 음수끼리 곱하기
for i in range(0, len(minus), 2):
    if i == len(minus) - 1:
        if not len(zero):
            ans+=minus[i]
    else:
        ans+=(minus[i] * minus[i+1])

print(ans)
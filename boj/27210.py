# 19분
N=int(input())
chart=list(map(int, input().split()))

# 이거면 1 기준 2 기준으로 하면 될 듯?

one=[0 for i in range(N)]
two=[0 for i in range(N)]

if chart[0] == 1:
    one[0]=1
else:
    two[0]=1

for idx, val in enumerate(chart[1:], start=1):
    if val == 1:
        one[idx]=max(0, one[idx-1])+1
        two[idx]=two[idx-1]-1
    elif val == 2:
        one[idx]=one[idx-1]-1
        two[idx]=max(0, two[idx-1])+1

#print(one)
#print(two)

print(max(max(one), max(two)))
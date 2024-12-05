n=int(input())
li=[]


for i in range(n):
    li.append(list(input()))

left_end=n-1
high_end=n-1
right_end=0
low_end=0
cnt=0
for i in range(n):
    for j in range(n):
        if li[i][j] == 'G':
            left_end=min(left_end, j)
            right_end=max(right_end, j)
            cnt+=1
            high_end=min(high_end, i)
            low_end=max(left_end, i)

#print(left_end, right_end, low_end, high_end)
if cnt==1:
    print(0)
elif left_end == right_end:
    print(min(n-1-high_end, low_end))
elif high_end == low_end:
    print(min(n-1-left_end, right_end))
else:
    print(min(n-1-left_end, right_end) + min(n-1-high_end, low_end))
length=100

arr=[[0 for j in range(length)] for i in range(length)]

n=int(input())
li=[]

for i in range(n):
    t=list(map(int, input().split()))
    for j in range(t[0]-1, t[0]+9):
        for k in range(t[1]-1, t[1]+9):
            arr[j][k]=1

for i in range(1, length):
    for j in range(length):
        if arr[i][j] == 1:
            arr[i][j]+=arr[i-1][j]

# for c in arr:
#     print(c)

ans=0
def check(start_row, start_col):
    global length, arr, ans
    temp=arr[start_row][start_col]
    for i in range(start_col, length):
        if arr[start_row][i] == 0:
            break
        temp=min(temp, arr[start_row][i])
        ans=max(ans, (i-start_col+1) * temp)


for i in range(length):
    for j in range(length):
        if arr[i][j] > 0:
            check(i, j)

print(ans)
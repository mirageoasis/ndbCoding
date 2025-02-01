n, m = map(int, input().split())

li=[]
for i in range(n):
    li.append(list(map(int, list(input().strip()))))
cnt=0
#print(li)
#print(li)
while True:
    #print(li)
    flag=True
    for row in range(n-1, -1, -1):
        for col in range(m-1, -1, -1):
            # i j 정하고
            if li[row][col] == 1:
                flag=False
                break
        if not flag:
            break
    else:
        break
    for i in range(row+1):
        for j in range(col+1):
            li[i][j]^=1
    cnt+=1

print(cnt)
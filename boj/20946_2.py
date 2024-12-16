import math
n=int(input())

# n sqrt까지 수를 구하면 소인수를 구할 수 있다.

limit=math.ceil(math.sqrt(n))

chart=[True for i in range(limit+1)]

chart[0]=False
chart[1]=False
li=[]
for i in range(2, limit+1):
    if chart[i]:
        li.append(i)
        for j in range(i*2, limit+1, i):
            chart[j]=False

ans_list=[]
for i in li:
    while not n % i:
        n//=i
        ans_list.append(i)

if n != 1:
    ans_list.append(n)

#print(ans_list)
ans_list.sort()
if len(ans_list) < 2:
    print(-1)
else:
    if len(ans_list) % 2:
        for i in range(0, len(ans_list)-1, 2):
            if i + 3 == len(ans_list):
                print(ans_list[i] * ans_list[i+1] * ans_list[i+2] ,end=' ')
            else:
                print(ans_list[i] * ans_list[i+1] ,end=' ')
    else:
        for i in range(0, len(ans_list), 2):
            print(ans_list[i] * ans_list[i+1] ,end=' ')
    print()
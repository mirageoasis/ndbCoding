# 켜진거는 취소 못한다잉

# 1000000000

chart=[]

n=int(input())

for i in range(5):
    chart.append(list(input().strip()))
for i in range(5):
    for j in range(4*n-1):
        if chart[i][j] == '#':
            chart[i][j] = True
        else:
            chart[i][j] = False

flag=True
ans=0
# 들어가면 안되는거 
numbers=[]
#0
numbers.append({(1, 1), (2, 1), (3, 1)})
#1
numbers.append(
    {
    (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
    (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
    }
)
#2
numbers.append(
    {
    (1, 0), (1, 1),
    (3, 1), (3, 2),
    }
)
#3
numbers.append(
    {
    (1, 0), (1, 1),
    (3, 0), (3, 1),
    }
)
#4
numbers.append(
    {
    (0, 1), (1, 1),
    (3, 0), (3, 1),
    (4, 0), (4, 1),
    }
)
#5
numbers.append(
    {
    (1, 1), (1, 2),
    (3, 0), (3, 1),
    }
)
#6
numbers.append(
    {
    (1, 1), (1, 2),
    (3, 1),
    }
)
#7
numbers.append(
    {
    (1, 0), (2, 0), (3, 0), (4, 0),
    (1, 1), (2, 1), (3, 1), (4, 1),
    }
)
#8
numbers.append(
    {
    (1, 1),(3, 1),
    }
)
#9
numbers.append(
    {
    (1, 1),
    (3, 1), (3, 0),
    }
)

for i in range(n):
    start_col=i*4

    marked=set()
    for j in range(5):
        for k in range(3):
            now_col = start_col + k
            if chart[j][now_col]:
                marked.add((j, k))
    can=[]
    for k in range(10):
        second_flag=True
        #print(marked, numbers[k])
        for m in marked:
            if m in numbers[k]:
                second_flag=False
        if second_flag:
            can.append(k)    
    #print(can)
    if not can:
        flag=False
        break
    
    ans*=10
    ans+=sum(can)/len(can)


if flag:
    print(ans)
else:
    print(-1)
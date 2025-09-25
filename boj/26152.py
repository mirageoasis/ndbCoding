n=int(input())
up=list(map(int, input().split()))
down=list(map(int, input().split()))
div=[]
INF=2500001
for i in range(n):
    div.append(up[i] - down[i])

m=int(input())
bird=list(map(int, input().split()))
new_bird=[]
for i in range(m):
    new_bird.append([bird[i], i, INF])

new_bird.sort()

# num 보다 큰 새를 찾는다. upper_bound

def cal(target):
    global n, new_bird, div, m
    start=0
    end=m
    while start < end:
        mid=(start+end)//2
        if target >= new_bird[mid][0]:
            start=mid+1
        else:
            end=mid
    
    return start

for i in range(n):
    num = div[i]
    k = cal(num)
    if k < m:
        new_bird[k][2]=min(new_bird[k][2], i)

now_num=INF
for i in range(m):
    if new_bird[i][2] == INF:
        new_bird[i][2]=n

for i in range(m):
    now_num=min(now_num, new_bird[i][2])
    new_bird[i][2]=now_num

new_bird.sort(key=lambda x: x[1])

ans=[i[2] for i in new_bird]

for i in ans:
    print(i)

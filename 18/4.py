N=int(input())

# 

li = []
chart = []

for _ in range(N):
    temp = list(map(int, input().split()))
    #print(temp)
    temp.append(_)
    li.append(temp)

#print(li)

for i in range(3):
    # li 정렬
    li.sort(key=lambda x: x[i])
    chart.append()


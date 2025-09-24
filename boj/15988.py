n=int(input())


chart=[0 for j in range(1000000+1)]
chart[0]=0
chart[1]=1
chart[2]=2
chart[3]=4

for i in range(4, 1000000+1):
    chart[i]=(chart[i-1] + chart[i-2] + chart[i-3]) % 1000000009

for _ in range(n):
    num=int(input())
    print(chart[num])
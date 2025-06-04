import sys

input=sys.stdin.readline

n=int(input())
li=list(map(int, input().split()))
cost=int(input())

chart=[0 for i in range(cost+1)]

def cal(c):
    global n, li
    if chart[c] != 0:
        return chart[c]
    if c == 0:
        return 0
    maxi=0
    for i in range(n):
        if c - li[i] >= 0:
            temp_c = str(cal(c-li[i]))
            ret=0
            if (int(temp_c[0]) <= i):
                ret=int(str(i)+temp_c)
            else:
                ret=int(temp_c+str(i))
            maxi=max(maxi, ret)
    chart[c]=maxi
    return chart[c]

print(cal(cost)//10)
#print(chart)
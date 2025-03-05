import sys
input=sys.stdin.readline
n=int(input())

def cal(start, end, num):
    if end-start == 1:
        return True
    
    mid=(start+end)//2
    for i in range(0, mid-start):
        s=num[start+i]
        e=num[end-1-i]
        if s == e:
            return False

    return cal(start, mid, num) and cal(mid+1, end, num)

for i in range(n):
    num=input().strip()
    #print(0, len(num))
    print("YES" if cal(0, len(num), num) else "NO")
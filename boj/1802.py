import sys
input=sys.stdin.readline

n=int(input())

def find(string):
    if len(string) == 1:
        return True
    mid=len(string)//2
    
    for i in range(1, mid+1):
        left=string[mid-i]
        right=string[mid+i]
        if left == right:
            return False
    else:
        return find(string[:mid]) and find(string[mid+1:])

# 3000 * 100
for i in range(n):
    string=input().strip()
    
    print("YES" if find(string) else "NO")

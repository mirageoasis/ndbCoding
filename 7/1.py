import sys

def find(store, first, last, target):
    if first > last:
        return False
    mid = (first + last) // 2
    if store[mid] > target:
        return find(store, first, mid - 1, target)
    elif store[mid] < target:
        return find(store, mid + 1, last, target)
    else:
        return True

N=int(input())
store=list(map(int, sys.stdin.readline().rstrip().split()))
M=int(input())
req=list(map(int, sys.stdin.readline().rstrip().split()))




# sort 하기
store.sort()

for i in req:
    ans = "yes" if find(store, 0, N-1, i) else "no"
    print(ans, end=' ')
print()
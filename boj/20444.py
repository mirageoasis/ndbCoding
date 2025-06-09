import math
n, k = map(int, input().split())


def binary_search_one():
    global n, k
    start=0
    end=n//2
    #print(start, end)
    while start<=end:
        mid=(start+end)//2
        res=(n+1-mid)*(mid+1)
        if res > k:
            end=mid-1
        elif res < k:
            start=mid+1
        else:
            return True
    return False

print("YES" if binary_search_one() else "NO")
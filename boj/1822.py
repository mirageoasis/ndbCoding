N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

def binary_search(target):
    start=0
    end=len(b)-1

    while start<=end:
        mid = (start+end)//2

        if b[mid] == target:
            return True
        elif b[mid] > target:
            end=mid-1
        else:
            start=mid+1
    
    return False

ans=[]
for i in a:
    if not binary_search(i):
        ans.append(i)

print(len(ans))
print(' '.join([str(i) for i in ans]))

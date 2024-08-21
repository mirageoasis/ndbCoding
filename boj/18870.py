N=int(input())

li=list(map(int, input().split()))

# 1 000 000 

new=sorted(list(set(li)))
ans=[]

def binary_search(new, target):
    start = 0
    end = len(new) - 1
    ret=len(new)
    while start <= end:
        mid=(start+end)//2
        if new[mid] >= target:
            end=mid-1
            ret=min(mid, ret)
        else:
            start=mid+1
    return ret

for i in li:
    # new 에서 찾기
    ans.append(binary_search(new, i))

print(' '.join([str(i) for i in ans]))
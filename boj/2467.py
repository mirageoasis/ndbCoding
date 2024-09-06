from bisect import bisect_left, bisect_right

N=int(input())

li=list(map(int, input().split()))

left=[i for i in li if i < 0]
right=[i for i in li if i >= 0]

left.sort()
right.sort()

# 같거나 작은거
def find_left(target):
    start=0
    end=len(left)-1
    idx=len(left)-1
    while start<=end:
        mid=(start+end)//2
        if left[mid]>=target:
            if idx > mid:
                idx=mid
            start=mid+1
        else:
            end=mid-1
    
    return idx

# 큰거 중에 최소
def find_right(target):
    start=0
    end=len(left)-1
    idx=0
    while start<=end:
        mid=(start+end)//2
        #print(left[mid], target)
        if left[mid]<=target:
            if idx < mid:
                idx=mid
            end=mid-1
        else:
            start=mid+1
    
    return idx


if len(right) == 0:
    print(left[-2], left[-1])
elif len(left) == 0:
    print(right[0], right[1])
else:
    ans=9_000_000_001
    ans_pr=[-1, -1]
    for i in right:
        a=left[find_left(-i)-1]
        b=left[find_right(-i)]
        print(a, b, i)

        if abs(i + a) > abs(i + b):
            if abs(i + b) < ans:
                ans=abs(i + b)
                ans_pr[0]=b
                ans_pr[1]=i
        else:
            if abs(i + a) < ans:
                ans=abs(i + a)
                ans_pr[0]=a
                ans_pr[1]=i
    minus=9_000_000_001
    plus=9_000_000_001
    if len(left) > 1:
        minus=abs(left[-2] + left[-1])
    if len(right) > 1:
        plus=abs(right[0] + right[1])
    mini = min(minus, plus)

    if abs(ans) < mini:
        print(ans_pr[0], ans_pr[1])
    else:
        if minus < plus:
            print(left[-2], left[-1])
        else:
            print(right[0], right[1])
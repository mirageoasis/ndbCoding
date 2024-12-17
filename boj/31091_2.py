from bisect import bisect_left, bisect_right
n=int(input())
li=list(map(int, input().split()))

plus_list=[i for i in li if i > 0]
minus_list=[abs(i) for i in li if i <= 0]

plus_list.sort()
minus_list.sort()

def b_r(target_list, target):
    start=0
    end=len(target_list)

    while start < end:
        mid=(start+end)//2
        if target_list[mid] <= target:
            start=mid+1
        else:
            end=mid
    return start

def b_l(target_list, target):
    start=0
    end=len(target_list)

    while start < end:
        mid=(start+end)//2
        if target_list[mid] < target:
            start=mid+1
        else:
            end=mid
    return start


ans=[]
for i in range(0, n+1):
    plus_false=len(plus_list) - bisect_right(plus_list, i)
    minus_false=bisect_left(minus_list, i)
    #print(plus_false, minus_false, i)
    if i == plus_false + minus_false:
        ans.append(i)

print(len(ans))
print(*ans)
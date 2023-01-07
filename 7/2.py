ans = 0

def temp(x, mid):
    return x - mid if x > mid else 0

'''
def bin_search(length_list, start, end, target):
    mid = (start+end)//2
    res = sum([temp(i, mid) for i in length_list])
    global ans
    if res > target:
        ans = max(ans, mid)
        bin_search(length_list, mid+1, end, target)
    elif res < target:
        bin_search(length_list, start, mid-1, target)
    else:
        ans = max(ans, mid)
'''

N, M=map(int, input().split())
length_list = list(map(int, input().split()))

length_list.sort()

#bin_search(length_list, 0, length_list[-1], M)

start = 0
end = length_list[-1]

while start<=end:
    mid=(start+end)//2
    res = sum([temp(i, mid) for i in length_list])

    if res >= M:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1
# 이런 유형의 문제는 recursive 보다 반복문으로 푸는게 낫다

print(ans)
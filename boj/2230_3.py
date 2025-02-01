import sys
n, m = map(int, input().split())
nums=[]
for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
from bisect import bisect_left
# xx보다 같거나 큰 수 중에서 제일 left
# xx보다 큰 수중에서 제일 left
mini=2000000001
for num in nums:
    idx=bisect_left(nums, num+m)
    if idx != len(nums):
        mini=min(nums[idx] - num, mini)

print(mini)
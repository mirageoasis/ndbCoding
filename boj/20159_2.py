n=int(input())
li=list(map(int, input().split()))

# 가장 아래 있는거
# 자신이 받을 카드를 안 받고 맨 밑에
# 10만개

# 이거 부분합?
"""
3 2 5 2 1 3
origin 3 5 1

3|2 2
"""
# 0부터 2까지
my_plus=[0]
other_plus=[0]

for i in range(n-1):
    if i % 2 == 0:
        my_plus.append(li[i])
    else:
        other_plus.append(li[i])

maxi=sum([li[i] for i in range(0, n, 2)])

for i in range(1, len(my_plus)):
    my_plus[i]+=my_plus[i-1]

for i in range(1, len(other_plus)):
    other_plus[i]+=other_plus[i-1]
#print(my_plus, other_plus)
for i in range(0, n):
    # 0 2 4
    if i % 2 == 0:
        my_sum=my_plus[i//2]
        other_sum=other_plus[len(other_plus)-1] - other_plus[i//2]
        #print(my_sum, other_sum, i//2, li[n-1])
        maxi=max(maxi, my_sum+other_sum+li[n-1])
    else:
        my_sum=my_plus[i//2+1]
        other_sum=other_plus[len(other_plus)-1] - other_plus[i//2]
        #print(my_sum, other_sum, i//2, li[n-1])
        #print(my_sum+other_sum)
        maxi=max(maxi, my_sum+other_sum)

"""
3 2 5 2 1 3

3 2 2
3 
"""

print(maxi)
import sys

N, order_cnt = map(int, input().split())

parents = list(map(int, input().split()))
parents.insert(0, 0)
orders=[]

for i in range(order_cnt):
    orders.append(list(map(int, sys.stdin.readline().split())))


print(parents)
print(orders)

info_dict = dict()
# 각각 depth도 포함시항
for i in range(1, N+1):
    # parent, auth, near_child
    info_dict[i]
import sys

N=int(input())
li = []

'''
1 1 0 0
11
10
10
10
10
00
'''

for i in range(N):
    li.append(bin(int(sys.stdin.readline())))
temp = [list(reversed([int(j) for j in  i[2:]])) for i in li]
#print(temp)
max_len = max([len(i) for i in temp])
#print(max_len)
one_list = [0 for _ in range(max_len)]

# 백만 * 백만 // 2 

# 뒤에서 부터 계산을 하자
ans=0

for i in temp:
    for idx, j in enumerate(i):
        if j == 1:
            one_list[idx]+=1

#print(one_list)
ans=0
for i in range(max_len):
    one_count = one_list[i]
    two_count = N - one_count
    ans+=2 ** i * one_count * two_count
print(ans)
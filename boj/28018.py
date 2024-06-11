#34
import sys

N=int(input())

student_chart=[]

#100000
for i in range(N):
    student_chart.append(list(map(int, sys.stdin.readline().split())))

Q=int(input())
time_chart=list(map(int, input().split()))

# test case를 담은게 time_chart

# 0 1 2 3 4 5 6 7 8 9 10
# 0 1 0 1 0 -1 -1 0 0 0 0

# 0 1 2 3 4 5 6 7
# 0 1 1 2 2 1 0 0 
LIM=1_000_002
dp=[0 for i in range(LIM)]

for s, e in student_chart:
    dp[s]+=1
    dp[e+1]-=1

for i in range(1, LIM):
    dp[i]+=dp[i-1]
#print(dp[:10])

for t in time_chart:
    print(dp[t])
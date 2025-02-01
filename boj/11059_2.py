"""1000 * 1000
1000 탐색 -> 시간 초과
전의 계산결과를 활용하는 법이 없나?

앞의 합과 뒤의 합을 어캐 알아내지?
부분합
i j 를 고르고 -> 1000 * 1000 
-> 중간을 찾는다. 그리고 부분합으로 해결 -> 연속되어있다.
"""
li=list(map(int, list(input())))
chart=[0 for i in range(len(li)+1)]

for i in range(1, len(li)+1):
    chart[i]=chart[i-1]+li[i-1]
# [0,i)로 표기

# mid를 구하고 
ans=0
for i in range(len(li)):
    for j in range(i+1, len(li), 2):
        origin=chart[j+1] - chart[i]
        half_idx=(i+j)//2
        half_val=chart[half_idx+1] - chart[i]
        #print(origin, half_val)
        if origin == half_val * 2:
            ans=max(ans, j-i+1)

print(ans)
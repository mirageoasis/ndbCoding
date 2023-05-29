# 서로소 개수
# 메모이제이션

from math import gcd

# def finder(i, j):
#     a = max(i, j)
#     b = min(i, j)
#     while True:
#         if a % b != 0:
#             temp = a % b
#             a = b
#             b = temp
#         else:
#             break
#     if b == 1:
#         return True
#     return False


N = int(input())

chart = [[False for i in range(1001)] for j in range(1001)]

for i in range(1,1001):
    for j in range(1,1001):
        if gcd(i, j) == 1:
            chart[i][j] = True

# 이렇게 안하고도 누적합을 통해 풀이가 가능하다. 
# 왜냐하면 전의 요소를 그대로 뒤에서도 활용하므로 뒤에서 나타난 요소에 대해서만 덧셈을 수행하면 되기 때문

for _ in range(N):
    T = int(input())
    cnt=0
    for i in range(1,T+1):
        for j in range(i+1,T+1):
            if chart[i][j]:
                cnt+=1
            
    print(cnt*2+3)
# 4와 7
# 10 ^ 9

# 4 -> 1
# 7 -> 2

# 4 4 -> 3
# 4 7 -> 4
# 7 4 -> 5
# 7 7 -> 6   2 * 2

# 4 4 4 -> 7
# 4 4 7 -> 8
# 4 7 4 -> 9
# 4 7 7 -> 10

# 7 4 4 -> 11
# 7 4 7 -> 12
# 7 7 4 -> 13
# 7 7 7 -> 14 -> 2 * 2 * 2

# 4 4 4 4 -> 15

# 1 -> 1번째 자리
# 3 -> 2번째 자리

# n 번째 자리 구하기

N = int(input())

dp = [2 ** i for i in range(100)]

temp_N = N
digit_number = 1

while True:
    temp_N -= 2 ** digit_number
    if temp_N <= 0:
        break
    digit_number+=1


#print(digit_number)

ans=""



s = sum(dp[1:digit_number])
N-=s
# 나머지 자리 계산
for i in range(digit_number - 1, 0, -1):
    if N > dp[i]:
        N-=dp[i]
        ans+="7"
    else:
        ans+="4"
if N == 2:
    ans+="7"
else:
    ans+="4"

print(ans)
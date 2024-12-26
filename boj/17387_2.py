
# x번 째 자리까지 존재하는 1의 개수
dp = [0 for i in range(100)]

dp[0]=0
dp[1]=1

for i in range(2, 100):
    dp[i]=2**(i-1)+dp[i-1]

for i in range(1, 100):
    dp[i]+=dp[i-1]

# 그리고 부분합 쓰기
a, b = map(int, input().split())
first_bin=bin(a)[2:]
second_bin=bin(b)[2:]

def recursive_plus(number_string, idx):
    global dp
    if idx == len(number_string):
        return 0
    # print(type(number_string))
    before_one=number_string[:idx].count('1')

    return before_one * (2**(len(number_string)-idx-1)) * int(number_string[idx]) + recursive_plus(number_string, idx+1)

print(recursive_plus(second_bin, 0) - recursive_plus(first_bin, 0) + second_bin.count('1'))
print()
print(recursive_plus(second_bin, 0))
print(recursive_plus(first_bin, 0))
print(second_bin.count('1'))
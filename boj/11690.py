# 관점을 바꾸긴했는데 메모리를 줄이지 못했다.
n = int(input())
prime = [bytearray(1) for i in range(n + 1)]  # True = 1, False = 0
ans = 1
MOD = 2**32

for i in range(2, n + 1):
    if prime[i]:
        for j in range(i * 2, n + 1, i):
            prime[j] = 0  # False

        s = 1
        for j in range(1, n + 1):
            s *= i
            if s > n:
                s //= i
                ans *= s
                ans %= MOD
                break

print(ans)

# 에라토스태네스

# dp를 활용?
# 역으로 발상...

n=int(input())
ans=0
for i in range(2, n+1):
    # n까지 개수를 구하기
    ans+=(((n // i) - 1) * i) % 1_000_000

print(ans% 1_000_000)
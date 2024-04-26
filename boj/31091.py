
N = int(input())
nums = list(map(int, input().strip().split(' ')))

center_chart = [0 for i in range(N+1)]
bigger_chart = [0 for i in range(N+1)]
smaller_chart = [0 for i in range(N+1)]

for i in nums:
    if i > 0:
        bigger_chart[i - 1] += 1
    else:
        smaller_chart[-i + 1] += 1

for i in range(1, N + 1):
    smaller_chart[i] += smaller_chart[i - 1]

for i in range(N - 1, -1, -1):
    bigger_chart[i] += bigger_chart[i + 1]

for i in range(0, N+1):
    center_chart[i] = bigger_chart[i] + smaller_chart[i]

ans = [str(i) for i in range(N+1) if i == center_chart[i]]

# print(bigger_chart)
# print(smaller_chart)
# print(center_chart)
print(len(ans))
print(' '.join(ans))
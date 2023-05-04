N = int(input())

days = [0 for _ in range(N)]
costs = [0 for _ in range(N)] 
total = [0 for _ in range(N+1)]

for i in range(N):
    days[i], costs[i] = map(int, input().split())

#print(days)
#print(costs)

# for i in range(N):
#     target_day = i + days[i]
#     if target_day <= N:
#         for j in range(target_day, N + 1):
#             total[j] = max(total[j], costs[i] + total[i])
    #print(total)

for i in range(N - 1, -1, -1):
    if i + days[i] > N:
        total[i] = total[i+1]
    else:
        total[i] = max(total[i + 1], total[i + days[i]] + costs[i])
#print("=" * 30)
print(total[0])
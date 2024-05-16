string = input()
N=int(input())

chart = []
ans=0

for i in range(N):
    a, b = input().split()
    chart.append((a, int(b)))

chart.sort(key=lambda x: (x[1] / len(x[0]), -len(x[0])), reverse=True)

chart = [c for c in chart if (c[1] / len(c[0])) > 1]
#print(chart)

dp = [-1 for i in range(len(string))]
#print(chart)

def cal(idx):
    if idx >= len(string):
        return 0

    if dp[idx] != -1:
        return dp[idx]
    
    for temp_string, score in chart:
        #print(temp_string, score)
        if string[idx:idx+len(temp_string)] == temp_string:
            dp[idx] = max(dp[idx], cal(idx+len(temp_string)) + score)
    dp[idx] = max(cal(idx+1) + 1, dp[idx])

    return dp[idx]

cal(0)
#print(dp)
print(max(dp))
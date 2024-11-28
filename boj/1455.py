n, m = map(int, input().split())

chart=[]

for i in range(n):
    chart.append(list(map(int, list(input()))))

# 1만 * 
ans=0
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):

        if chart[i][j] == 1:
            for k in range(i, -1, -1):
                for l in range(j, -1, -1):
                    chart[k][l] ^= 1
            ans+=1

print(ans)
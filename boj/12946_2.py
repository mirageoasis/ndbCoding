n=int(input())
chart=[]
visit=[[False for i in range(n)] for j in range(n)]
for i in range(n):
    chart.append(list(input()))


d_r=[1, -1, 0, 0, 1, -1]
d_c=[0, 0, -1, 1, -1, 1]

for i in range(n):
    for j in range(n):
        if chart[i][j] == 'X':
            num=[False, False, False]
            for k in range(6):
                new_row = i+d_r[k]
                new_col = j+d_c[k]
                if 0<=new_row<n and 0<=new_col<n:
                    if chart[new_row][new_col] == 0 or chart[new_row][new_col] == 1 or chart[new_row][new_col] == 2:
                        num[chart[new_row][new_col]]=True
            
            for k in range(3):
                if not num[k]:
                    chart[i][j]=k
                    break
ans=-1
for i in range(n):
    for j in range(n):
        if chart[i][j] == 0 or chart[i][j] == 1 or chart[i][j] == 2:
            ans=max(ans, chart[i][j])

print(ans+1)
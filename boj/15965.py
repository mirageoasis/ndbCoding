LIM=9999999

chart=[True for i in range(LIM)]
ans_chart=[]
N=int(input())

chart[0]=False
chart[1]=False

for i in range(2, LIM):
    if chart[i]:
        for j in range(i*2, LIM, i):
            chart[j]=False

ans=0
ans_chart.append(-1)
for i in range(LIM):
    if chart[i]:
        ans_chart.append(i)

print(ans_chart[N])
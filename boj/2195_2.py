s=input()
t=input()

chart=set()

for i in range(len(s)):
    start=s[i]
    chart.add(start)
    for j in range(i+1, len(s)):
        start+=s[j]
        chart.add(start)

temp=""
ans=0
for i in range(len(t)):
    if temp+t[i] not in chart:
        #print(i, temp)
        temp=t[i]
        ans+=1
    else:
        temp+=t[i]
#print(chart)
ans+=1
print(ans)
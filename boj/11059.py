
s=list(map(int, list(input())))

sum_chart=[0]+s

for i in range(1, len(sum_chart)):
    sum_chart[i]+=sum_chart[i-1]

#print(sum_chart)
ans=0
for i in range(len(s)):
    for j in range(i, len(s)):
        if (j - i + 1) % 2 == 0:
            mid=(j+i)//2
            #[:mid]
            #[]
            front=sum_chart[mid+1]-sum_chart[i]
            back=sum_chart[j+1]-sum_chart[mid+1]
            if front == back:
                #print(i, j)
                ans=max(ans, (j - i + 1))

print(ans)
n=int(input())
li=[]
for i in range(n):
    per, date, month, year = input().split()
    li.append((per, int(date), int(month), int(year)))

li.sort(key=lambda x: (x[3], x[2], x[1]))

#print(li)

print(li[-1][0])
print(li[0][0])
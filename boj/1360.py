n=int(input())

que=[('', 0)]

for i in range(n):
    c, letter, time = input().split()
    time=int(time)
    if c == 'type':
        que.append((que[-1][0] + letter, int(time)))
    
    if c == 'undo':
        rev=[]
        letter=int(letter)
        for i in range(len(que)-1, -1, -1):
            l_s, t_s = que[i]
            if t_s <= time - letter - 1:
                que.append((l_s, time))
                break
        else:
            que.append(('', time))
#print(que)

ans=[]
#print(que)
for q in que:
    letter, time = q
if que:
    print(que[-1][0])
else:
    print()
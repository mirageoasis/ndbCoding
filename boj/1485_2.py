t=int(input())

for i in range(t):
    li=[]
    li.append(list(map(int, input().split())))
    li.append(list(map(int, input().split())))
    li.append(list(map(int, input().split())))
    li.append(list(map(int, input().split())))

    line=[]
    for i in range(4):
        for j in range(i+1, 4):
            dist=(li[i][0] - li[j][0])**2 + (li[i][1] - li[j][1])**2
            line.append(dist)

    line.sort()
    #print(line)
    if (line[0] == line[1] == line[2] == line[3]) and (line[4] == line[5]):
        print(1)
    else:
        print(0)
N = int(input())


for _ in range(N):
    li = []
    k = []
    for x in range(4):
        li.append(list(map(int, input().split(' '))))
    
    for i in range(4):
        for j in range(4):
            k.append((li[i][0] - li[j][0]) ** 2 + (li[i][1] - li[j][1]) ** 2)
    k.sort()

    if k[4] == k[5] == k[6] == k[7] == k[8] == k[9]== k[10] == k[11] and (k[4] + k[5] == k[12]):
        print(1)
    else:
        print(0)

    # 16개
    # 4개는 0
    # 8개는 1
    # 4개는 루트 2
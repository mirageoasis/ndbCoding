#맨 앞에 있는 친구
N, K = map(int, input().split())
li = list(range(1, N+1))

end=N-1
cnt=0
while True:
    for i in range(0, end):
        if cnt == K:
            break
        temp = li[i]
        li[i] = li[i+1]
        li[i+1] = temp
        cnt+=1
    if cnt == K:
        break
    #print(cnt)
    end-=1

print(' '.join([str(x) for x in li]))
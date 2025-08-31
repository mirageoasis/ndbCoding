n=list(map(ord, list(input())))
visit=[False for i in range(len(n))]

index=-1
val=ord('Z') + 1
for i in range(len(n)):
    if val > n[i]:
        val=n[i]
        index=i

print(chr(val))
visit[index]=True
cnt=1
while cnt < len(n):

    #오른에서 찾기
    right_idx=-1
    #왼쪽에서 찾기
    left_idx=-1
    right_val=ord('Z') + 1
    left_val=ord('Z') + 1

    for i in range(index+1, len(n)):
        if not visit[i] and right_val > n[i]:
            right_val=n[i]
            right_idx=i
    start_left=-1
    for i in range(index-1, -1, -1):
        if not visit[i]:
            start_left=i
            break

    for i in range(start_left, -1, -1):
        if visit[i]:
            break
        if not visit[i] and left_val >= n[i]:
            left_val=n[i]
            left_idx=i
    
    if right_idx == -1:
        visit[left_idx]=True
        index=left_idx
    else:
        visit[right_idx]=True
        index=right_idx
    
    for i in range(len(n)):
        if visit[i]:
            print(chr(n[i]),end='')
    print()
    #print(visit)

    cnt+=1 
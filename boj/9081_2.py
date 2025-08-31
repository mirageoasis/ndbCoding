n=int(input())

for _ in range(n):
    li=list(map(ord, list(input())))
    # 자신보다 크면서 제일 낮은거 / 그리고 정렬

    # 늘어나는 마지막 index찾기
    change_idx=-1
    for i in range(len(li)-1):
        if li[i] < li[i+1]:
            change_idx=i
    
    if change_idx == -1:
        print(''.join(list(map(chr, li))))
    else:
        pick_val=li[change_idx+1]
        real_idx=change_idx+1
        for i in range(change_idx+1, len(li)):
            if pick_val > li[i] and li[i] > li[change_idx]:
                pick_val=li[i]
                real_idx=i

        temp=li[change_idx]
        li[change_idx]=pick_val
        li[real_idx]=temp
        first=li[:change_idx+1]
        second=list(sorted(li[change_idx+1:]))
        
        print(''.join(list(map(chr, first+second))))


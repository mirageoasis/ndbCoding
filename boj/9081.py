n=int(input())

for _ in range(n):
    li=list(input())
    # 글자가 올라가는게 ㅇㅇ
    
    next_list=[]
    find_idx=-1
    for i in range(len(li)-1):
        if li[i] < li[i+1]:
            find_idx=i
    # 가장 뒤에 나오는 친구
    
    if find_idx == -1:
        print(''.join(li))
        continue
    
    # 이제 시작 find_idx+1에서 부터
    change_idx=find_idx+1
    for i in range(find_idx+1, len(li)):
        if li[find_idx] < li[i] and li[change_idx] > li[i]:
            change_idx=i
    temp_li = li[find_idx:change_idx]
    if change_idx != len(li) - 1:
        temp_li += li[change_idx+1:]
    new_li = li[:find_idx] + [li[change_idx]] + list(sorted(temp_li))
    print(''.join(new_li))
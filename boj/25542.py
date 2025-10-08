n, m = map(int, input().split())
li=[]
for i in range(n):
    li.append(list(input()))
flag=False
ans=""

for i in range(m):
    # i 를 정해서 거기만 다르게 한다.
    for j in range(ord('A'), ord('Z')+1):
        string_list=li[0][:i] + [chr(j)] + li[0][i+1:]
        temp_flag=True
        for k in range(n):
            # 단어마다 check
            cnt=0
            for l in range(m):
                if string_list[l] != li[k][l]:
                    cnt+=1
            if cnt > 1:
                temp_flag=False
        flag=temp_flag
        if flag:
            ans=string_list
            break

    if flag:
        break

if flag:
    print(''.join(ans))
else:
    print("CALL FRIEND")

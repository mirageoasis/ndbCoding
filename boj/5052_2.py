import sys
input=sys.stdin.readline

t=int(input())

for _ in range(t):
    a=int(input().strip())
    now_node=1
    MAX=100004
    mapper=[[-1 for i in range(11)] for j in range(MAX)]
    chk=[False for i in range(MAX)]
    flag=True
    li=[]
    for i in range(a):
        string=input().strip()
        li.append(string)
    li.sort(key=lambda x: len(x))
    
    for string in li:
        now_num=0
        for s in string:
            new_char_num=int(s)
            if mapper[now_num][new_char_num] == -1:
                mapper[now_num][new_char_num]=now_node
                now_num=now_node
                now_node+=1
            else:
                # 만약에 왔던 길이면 chk들어간다.
                #print(now_num, chk[now_num], mapper[now_num][new_char_num])
                if chk[mapper[now_num][new_char_num]]:
                    flag=False
                now_num=mapper[now_num][new_char_num]

        chk[now_node-1]=True
        #print(chk[:20])


    print("YES" if flag else "NO")

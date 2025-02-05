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
    li.sort(key=lambda x:len(x))
    for string in li:
        now_idx=0
        for s in string:
            now_num=int(s)
            #print(now_idx)
            value=mapper[now_idx][now_num]
            if value == -1:
                mapper[now_idx][now_num]=now_node
                now_node+=1
            else:
                if chk[value]:
                    #print(s, " string: ", string)
                    flag=False
                    break
            now_idx=mapper[now_idx][now_num]
        if flag:
            chk[now_idx]=True

    print("YES" if flag else "NO")

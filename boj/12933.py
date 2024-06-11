#q u a c k
string=input()

N=len(string)
chart = list(string)
visited = [False for i in range(N)]
flag=True

ans=0

for i in range(N):
    if not visited[i]:
        if chart[i] != 'q':
            #print(chart[i], i)
            flag=False
            break
        else:
            # 여기서부터 시작
            temp_str=chart[i]
            li=[]
            visited[i]=True
            dic={
                'q': 'k',
                'u': 'q',
                'a': 'u',
                'c': 'a',
                'k': 'c'
            }
            for j in range(i+1, N):
                if not visited[j]:
                    now_char=chart[j]
                    if temp_str[-1] == dic[now_char]:
                        temp_str+=now_char
                        li.append(j)
                        
                        if now_char=='k':
                            for v in li:
                                visited[v]=True
                            li.clear()
            if len(temp_str) % 5 != 0:
                flag=False

            ans+=1

#print(ans)

if flag and ans != 0 and len(string) % 5 == 0:
    print(ans)
else:
    print(-1)
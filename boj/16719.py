string=list(map(ord, list(input())))
visit=[False for i in range(len(string))]

# 추가한 문자 중에서 자신보다 앞이냐 뒤냐

# 추가한 문자열.
# 탐색 시작할 위치

# 일단 뒤로 가서 시작. 하지만 만약에 뒤에가 막혀있다면 앞으로 돌아가기

# ord, chr
alpha=ord('Z')+1
idx=-1
for i in range(len(string)):
    if alpha > string[i]:
        alpha=string[i]
        idx=i
visit[idx]=True
cnt=1
print(chr(string[idx]))

if idx + 1 == len(string):
    idx=0
else:
    idx+=1

while cnt < len(string):
    former_idx=idx
    alpha=string[idx]
    #print(idx)
    for i in range(former_idx, len(string)):
        if visit[i]:
            break
        if alpha > string[i]:
            alpha=string[i]
            idx=i
    visit[idx]=True
    cnt+=1
    if idx + 1 == len(string) or visit[idx+1]:
        idx=0
        for i in range(len(string)-1):
            if visit[i] and not visit[i+1]:
                idx=i+1
    else:
        idx+=1

    for i in range(len(string)):
        if visit[i]:
            print(chr(string[i]) ,end='')
    print()

from functools import cmp_to_key
n, m = map(int, input().split())

def cmp(a, b):
    if len(a) != len(b):
        return len(a) - len(b)
    
    for i in range(min(len(a), len(b))):
        if a[i] != b[i]:
            return ord(a[i]) - ord(b[i])
    return -1

if n == m:
    print('0')
elif m == 0:
    print('-')
elif m == 1:
    print('/')
else:
    # *, + 순으로 간다.
    # bfs같이 visit 처리는 못할 듯? 메모리 터짐
    from collections import deque
    que=deque()
    que.append((1, '/'))
    que.append((n, ''))
    ans_list=[]
    while que:
        #print(que)
        num, string = que.popleft()
        #print(num, string)
        if num == m:
            ans_list.append(string)
            continue
        
        if num > m:
            continue
        
        if num * num <= m and num != 1:
            que.append((num*num, string+'*'))
        if num + num <=m:
            que.append((num+num, string+'+'))
    
    if len(ans_list):
        #print(ans_list)
        ans_list.sort(key=cmp_to_key(cmp))
        #print(ans_list)
        print(ans_list[0])
    else:
        print(-1)


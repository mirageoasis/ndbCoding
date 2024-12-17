from collections import deque

t=int(input())


for _ in range(t):

    n, m = map(int, input().split())
    li = list(map(int, input().split()))

    que=deque([(idx, val) for idx, val in enumerate(li)])
    ans=0
    while que:
        idx, val = que[0]
        flag=False
        for idx_new, val_new in list(que)[1:]:
            if val_new > val:
                flag=True
                break
        # 실패!
        if flag:
            que.append(que.popleft())
        else:
            ans+=1
            if idx==m:
                print(ans)
                break
            else:
                que.popleft()

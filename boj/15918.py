n, x, y = map(int, input().split())

ans = 0
arr = [-1 for i in range(n*2)]
visit = [False for i in range(n+1)]

target_number =  y - x - 1

arr[x - 1] = target_number
arr[y - 1] = target_number

visit[target_number] = True

def dfs(cnt):
    global ans
    global target_number
    if cnt == n+1:
        #print(arr)
        ans+=1
    # cnt마다 각각의 숫자를 고정시킨다는 생각을 하지 않고 모든 숫자를 넣게 되어서 오답이 나게 됨
    if cnt == target_number:
        dfs(cnt+1)
    else:
        for j in range(0, 2*n):
            if j+cnt+1 < 2*n and arr[j] == -1 and arr[j+cnt+1] == -1:
                arr[j] = arr[j+cnt+1] = cnt
                visit[cnt] = True
                dfs(cnt+1)
                visit[cnt] = False
                arr[j] = arr[j+cnt+1] = -1

dfs(1)

print(ans)
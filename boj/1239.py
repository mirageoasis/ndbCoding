from itertools import permutations

N = int(input())

li = list(map(int, input().split()))
# 50으로 만들어야한다.

ans = 0

for i in permutations(li, N):
    # 투포인터 - 1
    start = 0
    end = 1
    s = i[0]
    tempo = 0
    while start <= end:
        if s >= 50:
            if s == 50:
                tempo+=1
            s -= i[start]
            start += 1
        else:
            if end == N:
                break
            s += i[end]
            end += 1
    
    ans = max(ans, tempo - 1)


print(ans)
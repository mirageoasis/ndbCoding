N, M = map(int, input().split(' '))

li = list(map(int, input().split(' ')))

start = 0
end = 0 # 더할 예정지
summ = 0
ans = 0

while True:
    #print(start, end, summ)
    if summ < M:
        if end == N:
            break
        summ+=li[end]
        end+=1
    else:
        if summ == M:
            ans+=1
        summ-=li[start]
        start+=1

print(ans)
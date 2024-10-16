# 31분
integer_cache=[0 for i in range(1_00_001)]

N, K = map(int, input().split())

li=list(map(int, input().strip().split()))

#(start, end)
start=0
end=0
integer_cache[li[0]]+=1

length=-1

while start<=end:
    
    # 현재 상태 생각
    #print(start, end)
    #print(integer_cache[:3])
    if integer_cache[li[end]] > K:
        # start 땡긴다.
        while start<=end:
            integer_cache[li[start]]-=1
            if li[start] == li[end]:
                start+=1
                break
            start+=1
    else:
        length=max(length, end-start+1)
        if end == N-1:
            break
        end+=1
        integer_cache[li[end]]+=1


print(length)
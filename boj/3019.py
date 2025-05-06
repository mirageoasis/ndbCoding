import sys
input = sys.stdin.readline

n, m = map(int, input().split())
chart=list(map(int, input().split()))
d=dict()

# 0도 90도 180도 270도
# 전 단계에 비해서 얼마나 delta를 이루는지 알려준다.
# 맨 처음은 0
d[1]=[
    [0],
    [0,0,0,0],
]
d[2]=[
    [0, 0]
]
d[3]=[
    [0, 0, 1],
    [0, -1]
]
d[4]=[
    [0, 1],
    [0, -1, 0],
]
d[5]=[
    [0, 0, 0],
    [0, -1],
    [0, -1, 1],
    [0, 1]
]
d[6]=[
    [0, 0, 0],
    [0, -2],
    [0, 1, 0],
    [0, 0]
]
d[7]=[
    [0, 0, 0],
    [0, 0],
    [0, 0, -1],
    [0, 2]
]

ans=0
for li in d[m]:
    # 각각 경우를 count
    if len(li) == 1:
        ans+=n
        continue
    #print("jo")
    for start_idx in range(0, n-len(li)+1):
        prev=chart[start_idx]
        for j in range(1, len(li)):
            should_be=prev+li[j]
            if should_be != chart[start_idx+j]: 
                break
            prev=chart[start_idx+j]
        else:
            #print(start_idx)
            ans+=1
    #print(ans)
    #print("fin")
    #print()


    pass

print(ans)
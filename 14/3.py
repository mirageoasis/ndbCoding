from collections import defaultdict


def solution(N, stages):
    answer = []
    
    dic = defaultdict(int)
    li = []

    for i in stages:
        dic[i]+=1

    for i in range(1, N+1):
        tr = dic[i]
        fin = 0
        res = 0
        for j in range(i, N+2):
            fin += dic[j]    
        if fin:
            res = tr / fin
        
        li.append((i, res))

    li.sort(key=lambda x : (-x[1], x[0]))

    for k, v in li:
        answer.append(k)
    #print(li)

    return answer

print(solution(5 ,[2, 1, 2, 6, 2, 4, 3, 3]))
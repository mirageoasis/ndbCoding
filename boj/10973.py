import sys

N=int(input())

li = list(map(int ,sys.stdin.readline().strip().split(' ')))

#print(li)

def define_first(li):
    return all([idx == i for idx, i in enumerate(li, start=1)])

def cal(li : list):
    r = list(reversed(li))
    prev = r[0]
    t = []
    t.append(prev)
    for i in r[1:]:
        if i > prev:
            break
        else:
            t.append(i)
            prev = i
    
    # 역순으로 정렬
    idx = li.index(i)
    min_max = -1
    
    for j in t:
        if min_max < j and j < i:
            min_max = j
    
    t.remove(min_max)
    t.append(i)
    t.sort(reverse=True)
    new = li[:idx]
    new.append(min_max)
    new.extend(t)

    return ' '.join([str(i) for i in new])

if define_first(li):
    print(-1)
else:
    print(cal(li))

# 전의 수열은 역순 기준으로 처음으로 수가 증가 하는 곳 기준으로 끊는다.
# 그 다음 해당 수를 기준으로 나뉘어서 뒤의 수에서 해당 수보다 작은 수 중에 최대를 찾는다.
# 해당 수와 나뉘는 기준 수를 교환하고 내림차순으로 더함
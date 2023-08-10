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

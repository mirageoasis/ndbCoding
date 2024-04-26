from collections import deque


N = int(input())

for i in range(N):
    num, target = map(int, input().strip().split(' '))
    li = list(map(int, input().strip().split(' ')))

    heap = []
    t = deque()
    for idx, i in enumerate(li):
        t.append((idx, i))
        heap.append(i)
    heap.sort()

    n = 1
    while t:
        if heap[-1] == t[0][1]:
            if t[0][0] == target:
                print(n)
                break
            else:
                t.popleft()
                heap.pop()
                n+=1
        else:
            v = t.popleft()
            t.append(v)
        #print([-x for x in heap], t)





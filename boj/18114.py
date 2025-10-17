n, m = map(int, input().split())
li=list(sorted(list(map(int, input().split()))))

flag=0
# 1개
for i in li:
    if i == m:
        flag=1
        break

# 2개
if not flag:
    for i in range(len(li)):
        for j in range(i+1, len(li)):
            if li[i] + li[j] == m:
                flag=1
                break
# 3개

def binary(start, target):
    global li, n
    end=n
    while start < end:
        mid=(start+end)//2
        if li[mid] >= target:
            end=mid
        else:
            start=mid+1
    return start

if not flag:
    for i in range(len(li)-2):
        for j in range(i+1, len(li)-1):
            former = li[i] + li[j]
            target = m - former
            idx = binary(j+1, target)
            if idx != n and li[idx] + former == m:
                #print(flag)
                flag=1
                break


print(flag)
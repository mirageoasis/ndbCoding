N=int(input())
li=list(map(int, input().split()))

li.sort()

target = 1
for i in li:
    if i > target:
        break
    else:
        target+=i

print(target)
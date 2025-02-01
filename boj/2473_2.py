n=int(input())
li=list(map(int, input().split()))
li.sort()
mini=abs(li[0] + li[1] + li[2])
mini_list = [li[0], li[1], li[2]]

for i in range(n-2):
    start=i+1
    end=n-1
    while start < end:
        s=li[start]+li[end]
        if abs(s + li[i]) < mini:
            mini_list = [li[i], li[start], li[end]]
            mini=abs(s + li[i])
        if 0 < li[i] + s:
            end-=1
        elif 0 > li[i] + s:
            start+=1
        else:
            mini_list = [li[i], li[start], li[end]]
            mini=0
            break

print(*mini_list)

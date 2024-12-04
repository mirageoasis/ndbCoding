n=input()

li=list(map(int, input().split()))

last_inc_idx=0

if (list(sorted(li))) == li:
    print(-1)
else:
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            last_inc_idx=i
    
    #print(last_inc_idx)
    front_elem=li[:last_inc_idx]
    last_elem=li[last_inc_idx+1:]
    min_max=-1
    for i in last_elem:
        if i < li[last_inc_idx]:
            min_max=max(i, min_max)
    last_elem.remove(min_max)
    last_elem.append(li[last_inc_idx])

    print(' '.join([str(i) for i in front_elem + [min_max] + list(sorted(last_elem, reverse=True))]))


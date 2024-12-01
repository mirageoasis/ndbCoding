N=int(input())

li=list(map(int, input().split()))

zero_li=[i for i in li if i % 3 == 0]
one_li=[i for i in li if i % 3 == 1]
two_li=[i for i in li if i % 3 == 2]


if len(zero_li) == 0 and len(one_li) > 0 and len(two_li) > 0:
    print(-1)
elif len(zero_li) > len(one_li) + len(two_li) + 1:
    print(-1)
else:
    ans=[]
    if one_li:
        ans.append(one_li.pop())
    else:
        ans.append(two_li.pop())

    while len(zero_li) > 0:
        if len(zero_li) == 1:
            break
        
        if ans[-1] % 3 != 0:
            ans.append(zero_li.pop())
        else:
            if one_li:
                ans.append(one_li.pop())
            else:
                ans.append(two_li.pop())

    
    ans.extend(one_li)
    if ans[-1] % 3 != 0 and zero_li:
        ans.append(zero_li[0])
    elif ans[-1] % 3 == 0 and zero_li:
        ans.insert(0, zero_li[0])
    ans.extend(two_li)
    print(' '.join([str(a) for a in ans]))
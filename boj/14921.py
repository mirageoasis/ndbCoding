from bisect import bisect_left, bisect_right

N=int(input())
chart=list(map(int, input().split()))

minus=[i for i in chart if i < 0]
plus=[i for i in chart if i >= 0]

minus.sort()
plus.sort()

ans_list = []
ans_list.append(-99999999999)
ans_list.append(99999999999)
ans_list.append(99999999999)


if len(minus) > 1:
    ans_list[0]=minus[-1]+minus[-2]

if len(plus) > 1:
    ans_list[1]=plus[0]+plus[1]

if len(plus) > 0:    
    for i in minus:
        idx=bisect_left(plus, abs(i))
        #print(i)
        left=max(idx-1, 0)
        right=min(idx+1, len(plus)-1)
        mid=min(idx, len(plus)-1)

        temp=[plus[left]+i, plus[right]+i, plus[mid]+i]
        temp.sort(key=lambda x: (abs(x)))
        #print(temp)
        if abs(temp[0]) < abs(ans_list[2]):
            ans_list[2]=temp[0]

ans_list.sort(key=lambda x: (abs(x)))


print(ans_list[0])
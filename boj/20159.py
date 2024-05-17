N=int(input())
li = list(map(int, input().split()))
summon=[0 for i in range(N)]

even = sum([i for idx, i in enumerate(li) if idx % 2 == 0])
odd = sum([i for idx, i in enumerate(li) if idx % 2 != 0])
ans=even
# summon은 i부터 뒤까지
even_eraser=0
odd_eraser=0
for i in range(N):
    if i % 2 == 0:
        summon[i]=even-even_eraser-li[-1]
        even_eraser+=li[i]
    else:
        summon[i]=odd-odd_eraser-li[-1]
        odd_eraser+=li[i]

prev_sum=0
for idx, val in enumerate(li[:-1]):
    if idx % 2 == 0:
        #print(prev_sum+summon[idx+1]+li[-1])
        ans=max(ans, prev_sum+summon[idx+1]+li[-1])
        prev_sum+=val
    else:
        #print(summon[idx+1])
        #print(prev_sum+summon[idx+1])
        ans=max(ans, prev_sum+summon[idx+2]+li[idx+1])

#print(summon)
#print(li)
print(ans)
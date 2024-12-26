from itertools import permutations

n=int(input())

li=list(map(int, input().split()))

# n 범위가 작아서 브르투?
ans=0

for i in permutations(li):
    
    start=0
    end=0
    s=0
    temp_ans=0
    while True:
        if s <= 50:
            if s == 50:
                #print(start, end, i[start:end], i)
                temp_ans+=1
            if end == n:
                break
            s+=i[end]
            end=end+1
        else:
            s-=i[start]
            start+=1
    ans=max(temp_ans - 1, ans)

print(ans)
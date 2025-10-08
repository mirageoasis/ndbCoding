# 3가지

# 앞뒤를 제외하자구

n=int(input())
li=list(map(int, input().split()))
# 가지수

if n == 1 or n == 2:
    print(0)
    exit(0)


case=[]

# 9가지

for i in range(-1, 2):
    for j in range(-1, 2):
        flag=True
        new_arr=li.copy()
        new_arr[0]+=i
        new_arr[1]+=j
        cnt=abs(i) + abs(j)
        diff=new_arr[0] - new_arr[1]
        for k in range(2, len(new_arr)):
            first=new_arr[k-1]
            second=new_arr[k]
            new_diff = first - second
            delta=new_diff - diff
            #print(new_diff, diff, k)
            if abs(delta) > 1:
                flag=False
                break
            
            new_arr[k]+=delta
            cnt+=abs(delta)
        #print(new_arr)
        if flag:
            case.append(cnt)


#print(case)
if case:
    print(min(case))
else:
    print(-1)
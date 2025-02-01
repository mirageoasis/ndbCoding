# 아래 있는 결과를 활용할 수 있을 것 같음 -> dp
# 연속된 이니까 투포인터? 

n=int(input())
LIM=n+1
is_prime=[True for i in range(LIM)]
is_prime[0]=False
is_prime[1]=False
for i in range(2, LIM):
    for j in range(i*2, LIM, i):
        is_prime[j]=False
prime_list=[]
for i in range(2, LIM):
    if is_prime[i]:
        prime_list.append(i)
start=0
end=0
s=0
ans=0
while start <= end:
    if s < n:
        if end == len(prime_list):
            break
        s+=prime_list[end]
        end+=1
    else:
        if s == n:
            ans+=1
        s-=prime_list[start]
        start+=1
print(ans)
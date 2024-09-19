# 일단 자기 자신 보다 작은 소수를 찾아야겠지?
# 연속한 소수, naive하게 생각하면 N^2인데....

# 소수 목록 구하기

N=int(input())

is_prime=[True for i in range(N+1)]
prime=[]

is_prime[0]=False
is_prime[1]=False

for i in range(2, N+1):
    if is_prime[i]:
        for j in range(i*2, N+1, i):
            is_prime[j]=False

for i in range(2, N+1):
    if is_prime[i]:
        prime.append(i)

start=0
end=0
s=0
ans=0

while True:
    
    if s >= N:
        if s == N:
            ans+=1
        s-=prime[start]
        start+=1
    else:
        if end == len(prime):
            break
        s+=prime[end]
        end+=1

print(ans)
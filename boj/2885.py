k = int(input())

# 1 1 0
# 2 2 0
# 3 4 2
# 4 4 0
# 5 8 3
# 6 8 2

def small_2_pow(k):
    n=1
    while(n<k):
        n*=2
    return n

if small_2_pow(k) == k:
    print(k, 0)
else:
    n = small_2_pow(k)
    ans=n
    time=0
    while k > 0:
        if k >= n:
            k-=n
        else:
            n//=2
            time+=1
        

    print(ans, time)


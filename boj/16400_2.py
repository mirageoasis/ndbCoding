LIM=40001

is_prime=[True for i in range(LIM)]

for i in range(2, LIM):
    if is_prime[i]:
        for j in range(i*2, LIM, i):
            is_prime[j]=False

chart=[0 for i in range(LIM)]

chart[4]=1
chart[5]=1

for i in range(5, LIM):
    
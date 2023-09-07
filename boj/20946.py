LIM = 10**6+1

N = int(input())

chart = [False for _ in range(LIM)]
p_list = []


for i in range(2, LIM):
    if not chart[i]:
        p_list.append(i)
        for j in range(i*2, LIM, i):
            chart[j] = True

#print(p_list)
def make_temp_list(num):
    t_list = []

    for i in p_list:
        while num % i == 0:
            num //= i
            t_list.append(i)

    if num > 1:
        t_list.append(num)

    return t_list


temp_list = make_temp_list(N)
ans_list = []

if len(temp_list) < 2:
    ans_list.append(-1)
else:
    for i in range(0, len(temp_list), 2):
        if i == len(temp_list) - 1:
            ans_list[-1] *= temp_list[i]
        else:
            ans_list.append(temp_list[i] * temp_list[i+1])

print(' '.join([str(i) for i in ans_list]))

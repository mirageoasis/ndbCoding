N=int(input())
li = list(map(int, input().split()))

# 2 작은거
# 3 큰거

def two_cnt(num):
    ret = 0
    while True:
        if num % 2 != 0: 
            break
        num //= 2
        ret+=1

    return ret

def three_cnt(num):
    ret = 0
    while True:
        if num % 3 != 0: 
            break
        num //= 3
        ret+=1
    return ret

def temp(num):
    t_c = two_cnt(num)
    th_c = three_cnt(num)

    return (t_c, th_c, num)


new_li = list(map(temp, li))

new_li.sort(key=lambda x: (x[0], -x[1], x[2]))

print(' '.join([str(x[2]) for x in new_li]))
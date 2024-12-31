'''
4 -> 1 0
7 -> 2 1

x 자리수 맞추고
44 -> 3 00
47 -> 4 01
74 -> 5 10
77 -> 6 11

444 -> 7 000
447 -> 8 001
474 -> 9 010
477
744
747
774
777

2
4
8
16
'''

# 10 ^ 9 승 -> 그냥 계산하면 터짐
# 자리수 구하고
# 자리에서 몇번째 인지

number=int(input())

def biggest_two(number):
    cnt=1
    while 2**cnt < number:
        number-=2**cnt
        cnt+=1
    return cnt

def cal(number):
    if number == 1:
        return 4
    if number == 2:
        return 7
    
    bigg = biggest_two(number)
    #print(bigg)
    number -= 2**(bigg) - 2
    number-=1
    #print(number)

    binary=bin(number)[2:]
    binary = "0" * (bigg - len(binary)) + binary
    #print(binary)
    ans=""
    for i in binary:
        ans+= "7" if i == "1" else "4"
    return ans



print(cal(number))


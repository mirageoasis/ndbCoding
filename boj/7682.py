import sys

cases = []
converted_cases = []

while True:
    a = sys.stdin.readline().strip()
    if a == 'end':
        break
    cases.append(list(a))

def convert(i):
    first = [i[0], i[1], i[2]]
    second = [i[3], i[4], i[5]]
    third = [i[6], i[7], i[8]]
    return [first, second, third]

# converter
for i in cases:
    converted_cases.append(convert(i))

#print(converted_cases)
    

# 1. X O 의 개수 파악
# 2. 이미 게임이 끝난 경우인가.
#   -> 
    
def judge(cs, c:list):
    zero_count = c.count('O')
    x_count = c.count('X')
    # for i in cs:
    #     print(i)
    # x가 먼저, O가 나중 고로 x - o == 1 or 0
    if (zero_count + x_count) == 0:
        return False
    if x_count - zero_count != 1 and x_count - zero_count != 0:
        return False
    # 이제 이미 끝난 경우를 서술한다.
    # O가 이겼는데 x가 많은 경우 -> out

    def find(cs, target):
        for i in range(3):
            if cs[i][0] == cs[i][1] == cs[i][2] == target:
                return True
            if cs[0][i] == cs[1][i] == cs[2][i] == target:
                return True
        if cs[0][0] == cs[1][1] == cs[2][2] == target:
            return True
        if cs[0][2] == cs[1][1] == cs[2][0] == target:
            return True

        return False

    def find_o(cs):
        return find(cs, target='O')
    def find_x(cs):
        return find(cs, target='X')
    o_win = False
    x_win = False
    if find_o(cs):
        o_win=True
    if find_x(cs):
        x_win=True

    if x_win and o_win:
        return False
    
    if x_count - zero_count == 1 and x_win:
        return True

    if x_count - zero_count == 0 and o_win:
        return True

    if x_count == 5 and zero_count == 4 and not o_win and not x_win:
        return True

    return False


for cs, c in zip(converted_cases, cases):
    if judge(cs, c):
        print("valid")
    else:
        print("invalid")
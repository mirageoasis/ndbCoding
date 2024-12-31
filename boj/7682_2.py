# 최종 단계 판단

'''

XXX
OO.
XXX invalid

XOX
OXO
XOX valid

OXO
XOX
OXO invalid

XXO
OOX
XOX valid

XO.
OX.
..X valid

.XX
X.X
OOO invalid

X.O
O..
X.. invalid

OOX
XXO
OXO invalid

첫번째 x -> o보다 1개 많음
o는 x 보다 많아 질 수 없음

'''

# 맞았는데 chart 초기화를 안해서...
chart=[]

def winner(alpha):
    global chart

    # 대각선
    if chart[0][0] == chart[1][1] == chart[2][2] == alpha:
        return True

    if chart[0][2] == chart[1][1] == chart[2][0] == alpha:
        return True
    
    if chart[0][2] == chart[1][1] == chart[2][0] == alpha:
        return True
    
    for i in range(3):
        if chart[i][0] == chart[i][1] == chart[i][2] == alpha:
            return True
    
    for i in range(3):
        if chart[0][i] == chart[1][i] == chart[2][i] == alpha:
            return True
    

    return False

def cal(temp):
    global chart
    o_count = temp.count('O')
    x_count = temp.count('X')

    if o_count > x_count:
        return False
    
    o_winner = winner('O')
    x_winner = winner('X')

    #print(o_winner, x_winner)

    if x_count > o_count + 1:
        return False
    if o_count > x_count:
        return False

    if (not o_winner) and (not x_winner):
        if x_count == 5 and o_count==4:
            return True
        return False

    if o_winner and x_winner:
        return False
    
    if o_winner:
        if o_count != x_count:
            return False
        return True

    if x_winner:
        if x_count != o_count +1:
            return False

    return True


while True:
    temp = list(input())

    if temp == ['e', 'n', 'd']:
        break
    chart=[]
    chart.append(temp[:3])
    chart.append(temp[3:6])
    chart.append(temp[6:])
    print('valid' if cal(temp) else 'invalid') 

'''
XO.
X.O
XO.
'''
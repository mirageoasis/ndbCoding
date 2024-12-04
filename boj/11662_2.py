import math
import time

li=list(map(int, input().split()))

a=[li[0], li[1], li[2], li[3]]
b=[li[4], li[5], li[6], li[7]]

len_a = math.sqrt((li[0] - li[2])**2 + (li[1] - li[3])**2)
len_b = math.sqrt((li[4] - li[6])**2 + (li[5] - li[7])**2)

# t 는 0 부터 a 길이

a_x_delta=li[2]-li[0]
a_y_delta=li[3]-li[1]
b_x_delta=li[6]-li[4]
b_y_delta=li[7]-li[5]


start=0
end=100

def a_x_pos(cord):
    global len_a, a_x_delta 
    return a[0] + cord * a_x_delta / 100

def a_y_pos(cord):
    global len_a, a_y_delta 
    return a[1] + cord * a_y_delta / 100

def b_x_pos(cord):
    global len_a, b_x_delta, len_b
    return b[0] + cord * b_x_delta / 100

def b_y_pos(cord):
    global len_a, b_y_delta, len_b
    return b[1] + cord * b_y_delta / 100

def res(cord):
    a_x, a_y = a_x_pos(cord), a_y_pos(cord)
    b_x, b_y = b_x_pos(cord), b_y_pos(cord)
    return math.sqrt((a_x - b_x) ** 2 + (a_y - b_y) ** 2)

while True:
    one_third=start+((end-start) / 3)
    two_third=start+((end-start) * 2 / 3)

    one_res=res(one_third)
    two_res=res(two_third)
    #time.sleep(0.1)
    #print(start, end, one_third, two_third, one_res)
    if end - start <= 1e-10:
        print(one_res)
        break

    if one_res > two_res:
        start=one_third
    else:
        end=two_third
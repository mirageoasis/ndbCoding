x1, y1, x2, y2 = map(int, input().split(' '))
x3, y3, x4, y4 = map(int, input().split(' '))

def ccw(p1, p2, p3):
    # 시계면 음수
    # 반시계면 양수
    # 일직선이면 0
    a1, b1 = p1
    a2, b2 = p2
    a3, b3 = p3
    ret = (a1 * b2 + a2 * b3 + a3 * b1 - a2 * b1 - a3 * b2 - a1 * b3)
    # print(p1, p2, p3)
    # print(a1, b1, a2, b2)
    # print(ret)
    if ret < 0:
        return -1
    elif ret > 0:
        return 1
    else:
        return 0

p1 = (x1, y1)
p2 = (x2, y2)
p3 = (x3, y3)
p4 = (x4, y4)

cc1 = ccw(p1, p2, p3)
cc2 = ccw(p1, p2, p4)
cc3 = ccw(p3, p4, p1)
cc4 = ccw(p3, p4, p2)

#print(cc1, cc2, cc3, cc4)

ans = 0

if cc1 * cc2 == cc3 * cc4 == 0:
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        ans = 1
elif cc1 * cc2 <= 0 and cc3 * cc4 <= 0:
    ans = 1

print(ans)
from math import sqrt

Ax, Ay, Bx, By, Cx, Cy, Dx, Dy=map(int, input().split())

def minho(t):
    x = Ax + (Bx - Ax) * (t / 100)
    y = Ay + (By - Ay) * (t / 100)
    return x, y

def kangho(t):
    x = Cx + (Dx - Cx) * (t / 100)
    y = Cy + (Dy - Cy) * (t / 100)
    return x, y

lo=0
hi=100

while  hi - lo >= 1e-6:
    p = (lo * 2 + hi) / 3
    q = (lo + hi * 2) / 3
    #print(lo, hi)
    p_x = minho(p)[0] - kangho(p)[0]
    p_y = minho(p)[1] - kangho(p)[1]
    
    q_x = minho(q)[0] - kangho(q)[0]
    q_y = minho(q)[1] - kangho(q)[1]

    p_len = p_x ** 2 + p_y ** 2
    q_len = q_x ** 2 + q_y ** 2

    if p_len > q_len:
        lo=p
    else:
        hi=q

ans_x = minho(lo)[0] - kangho(lo)[0]
ans_y = minho(lo)[1] - kangho(lo)[1]


print(sqrt(ans_x ** 2 + ans_y ** 2))
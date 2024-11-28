import time
s=input()
t=input()

def cal(s, now):
    if len(now) == len(s):
        return 1 if now == s else 0
    #print(now)
    #time.sleep(0.5)
    ret = 0
    if now[0] == 'B':
        new=now[::-1]
        ret += cal(s, new[:-1])
    
    if now[-1] == 'A':
        ret += cal(s, now[:-1])
    return ret


ret = cal(s, t)

print(1 if ret else 0)
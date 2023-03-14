
def idx_return(string):
    cnt = 0
    temp = dict()
    temp["("] = 1
    temp[")"] = -1

    for idx ,i in enumerate(string):
        cnt += temp[i]
        if idx != 0 and cnt == 0:
            return idx

def def_right(string):
    temp = dict()
    temp["("] = 1
    temp[")"] = -1
    cnt = 0
    for i in string:
        cnt += temp[i]
        if cnt < 0:
            return False
    else:
        if cnt != 0:
            return False
        else:
            return True

def reverse(string):
    ret = ""
    temp = dict()
    temp["("] = ")"
    temp[")"] = "("
    for i in string:
        ret += temp[i]
    return ret

def rec(string):
    
    if string == "":
        return ""
    idx = idx_return(string)

    u = string[:idx+1]
    v = string[idx+1:]
    #print(u, v)
    if def_right(u):
        return u + rec(v)
    else:
        return "(" + rec(v) + ")" + reverse(u[1:-1])

def solution(p):
    answer = ''
    
    if p == "":
        return ""
    
    return rec(p)
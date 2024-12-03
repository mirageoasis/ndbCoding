# 10 ^ 9면 9자리 이므로 brute force 가능하지 않을까?

# 9 * 9 * 9 
# 

mini=9999999999999
maxi=-1

n=int(input())

def collector(string):
    return sum([1 for s in string if int(s) % 2])

def cal(n, cnt):
    global mini, maxi
    stringify=str(n)
    cnt_plus=collector(stringify)
    if len(stringify) == 1:
        mini=min(mini, cnt+ n%2)
        maxi=max(maxi, cnt+ n%2)
        return
    elif len(stringify) == 2:
        cal(int(stringify[0]) + int(stringify[1]), cnt+cnt_plus)
    elif len(stringify) >= 3:
        for i in range(len(stringify)):
            for j in range(i+1, len(stringify)-1):
                    f_res=stringify[0:i+1]
                    s_res=stringify[i+1:j+1]
                    t_res=stringify[j+1:]
                    # 개수 세기
                    fin = collector(f_res) + collector(s_res) + collector(t_res)
                    cal(int(f_res) + int(s_res) + int(t_res), cnt+fin)





cal(n, 0)

print(mini, maxi)
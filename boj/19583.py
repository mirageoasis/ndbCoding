# 40
import sys
def time_to_int(string):
    a, b = map(int, string.split(":"))

    return a * 60 + b

s,e,q=input().split()

s_num=time_to_int(s)
e_num=time_to_int(e)
q_num=time_to_int(q)

start_set=set()
end_set=set()

while True:
    try:
        i=sys.stdin.readline()
        if i == "\n":
            break
        t, name = i.split()
        t_num=time_to_int(t)
        #print(t_num, s_num, e_num, q_num)
        if t_num <= s_num:
            start_set.add(name)
        elif e_num<=t_num<=q_num:
            end_set.add(name)
    except:
        break



ans_set = start_set & end_set
#print(start_set)
#print(end_set)
print(len(ans_set))
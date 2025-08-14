# 

# 60개


def cal_slump(start, end):
    global string, is_slump
    if start >= end:
        return 0
    
    if is_slump[start][end] != -1:
        return is_slump[start][end]

    if string[start] != 'D' and string[start] != 'E':
        is_slump[start][end]=0
        return is_slump[start][end]
    
    if start == len(string) - 1 or string[start + 1] != 'F':
        is_slump[start][end]=0
        return is_slump[start][end]
    f_end_idx=start+1
    for i in range(start+1, end):
        if string[i] != 'F':
            f_end_idx=i
            break
        f_end_idx+=1

    if f_end_idx == end and string[f_end_idx] == 'G':
        is_slump[start][end]=1
        return is_slump[start][end]
    is_slump[start][end] = cal_slump(f_end_idx, end)
    return is_slump[start][end]

def cal_slimp(start, end):
    global string, is_slimp
    if is_slimp[start][end] != -1:
        return is_slimp[start][end]

    if string[start] != 'A':
        is_slimp[start][end]=0
        return is_slimp[start][end]

    if start + 1 == end and string[end] == 'H':
        is_slimp[start][end]=1
        return is_slimp[start][end]
    
    if string[start+1] == 'H':
        is_slimp[start][end] = 0
        return is_slimp[start][end]
    
    if start + 2 >= end:
        is_slimp[start][end] = 0
        return is_slimp[start][end]
    if string[start+1] == 'B':
        is_slimp[start][end] = cal_slimp(start + 2, end - 1) and string[end] == 'C'
        return is_slimp[start][end]
    is_slimp[start][end]=cal_slump(start+1, end-1) and string[end] == 'C'
    return is_slimp[start][end]




# 60 이하면 그냥 다 해보자
n=int(input())
is_slump=[]
is_slimp=[]
string=[]
print("SLURPYS OUTPUT")
for _ in range(n):
    string=list(input())
    is_slump=[[-1 for i in range(len(string))] for j in range(len(string))]
    is_slimp=[[-1 for i in range(len(string))] for j in range(len(string))]

    # -1이면 계산 안된거고 1이면 ㅇㅋ 0이면 x

    for i in range(len(string)):
        for j in range(i, len(string)):
            cal_slump(0, len(string)-1)
    
    #print(cal_slump(0, len(string)-1, string))
    
    for i in range(len(string)):
        for j in range(i, len(string)):
            cal_slimp(0, len(string)-1)
    
    flag=False

    for i in range(len(string) - 1):
        slimp_flag=cal_slimp(0,i)
        slump_flag=cal_slump(i+1,len(string)-1)
        #print(i, slimp_flag and slump_flag)
        flag |= slimp_flag and slump_flag

    print("YES" if flag else "NO")

print("END OF OUTPUT")
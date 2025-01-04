import sys

col_len=int(input())
row_len=int(input())

up_list=[chr(ord('A') + i) for i in range(col_len)]
down_list=list(input())

# 0 이면 0 1 바꾸고, 1이면 1 2 바꾼다.
#print(up_list)
#print(down_list)
down_command=[]
flag=True
for i in range(row_len):
    line=list(sys.stdin.readline())

    if line[0] == '?':
        flag=False
        continue
    if flag:
        # 위 바꾸기
        for i in range(col_len-1):
            if line[i] == '-':
                temp=up_list[i]
                up_list[i]=up_list[i+1]
                up_list[i+1]=temp
    else:
        # 아래 바꾸기
        down_command.append(line)

# 바꾸기
down_command.reverse()

for line in down_command:
    for i in range(col_len-1):
            if line[i] == '-':
                temp=down_list[i]
                down_list[i]=down_list[i+1]
                down_list[i+1]=temp

ans=""
red_flag=False
for i in range(col_len-1):
    if up_list[i] == down_list[i]:
        ans+="*"
        continue

    if not ((up_list[i] == down_list[i+1]) and (up_list[i+1] == down_list[i])):
        #print(i)
        #print(up_list)
        #print(down_list)
        red_flag=True
        break
    temp1=up_list[i]
    
    up_list[i]=up_list[i+1]
    up_list[i+1]=temp1
    #print(i, temp1, temp2)
    #print(up_list)
    #print(down_list)
    ans+='-'

if red_flag:
    print('x' * (col_len-1))
else:
    print(ans)
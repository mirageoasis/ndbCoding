# 248
# 255 -> 11111000

# 가장 작은 경우니까 가장 1이 왼쪽으로 나오는 케이스를 잡아야 한다.
import sys
n=int(input())

# 1000 * 8 * 4 = 32000
converted=[]
for i in range(n):
    t=sys.stdin.readline()
    t=list(map(int, t.split('.')))
    for j in range(4):
        c = bin(t[j])[2:]
        t[j] = '0' * (8-len(c)) + c 
    converted.append(''.join(t))

#print(converted)
ans_idx=0
for i in range(33):
    if i == 32:
        ans_idx=i
        break
    number=converted[0][i]
    flag=True
    for j in range(n):
        if number != converted[j][i]:
            flag=False
            break
    if not flag:
        break
    ans_idx=i+1

sub_net=''
sub_net+= '1' * (ans_idx)
sub_net+= '0' * (32-ans_idx)
#print(sub_net)
t_str=sub_net[:]
ans_str=''

for i in range(32):
    flag= True if t_str[i] == '1' else False
    for j in range(n):
        if converted[j][i] == '0':
            flag=False
            break
    if flag:
        ans_str+='1'
    else:
        ans_str+='0'
temp_str=[]
for i in range(4):
    start=i * 8
    #print(sub_net[start:start+8])
    temp_str.append(str(int(ans_str[start:start+8] ,2)))
print('.'.join(temp_str))

temp_str=[]
for i in range(4):
    start=i * 8
    #print(sub_net[start:start+8])
    temp_str.append(str(int(sub_net[start:start+8] ,2)))

print('.'.join(temp_str))
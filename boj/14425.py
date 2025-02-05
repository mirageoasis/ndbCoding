import sys
input=sys.stdin.readline

n, m = map(int, input().split())
"""
n번 노드 -> 노드는 문자열 길이 * 개수
0번은 빈 문자열
"""
MAX=500*10000+1
mapper = [[-1 for i in range(26)] for j in range(MAX)]
chk=[False for i in range(MAX)]
# mapper[x][y] -> x 번에 y 문자열을 가진 객체는 -> value번이랑 연결
node_number=1
ans=0
for i in range(n):
    string=input().strip()
    now_idx=0
    for s in string:
        char_num= ord(s) - ord('a')
        if mapper[now_idx][char_num] == -1:
            mapper[now_idx][char_num]=node_number
            node_number+=1
        
        now_idx=mapper[now_idx][char_num]
    chk[now_idx]=True

for i in range(m):
    string=input().strip()
    now_idx=0
    for s in string:
        char_num= ord(s) - ord('a')
        if mapper[now_idx][char_num] == -1:
            break
        now_idx=mapper[now_idx][char_num]
    else:
        #print(chk[now_idx])
        if chk[now_idx]:
            ans+=1

print(ans)
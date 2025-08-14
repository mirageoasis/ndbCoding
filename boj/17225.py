import sys
input=sys.stdin.readline

# 상민, 지수
a, b, n = map(int, input().split())

a_last_pack=0
b_last_pack=0
ans=[]

for _ in range(n):
    # x초 주문 먼저 받고 포장 시작
    a_t, b_t, amount = input().split()
    time, amount=int(a_t), int(amount)
    
    if b_t == 'B' and a_last_pack < time:
        a_last_pack=time
    elif b_t == 'R' and b_last_pack < time:
        b_last_pack=time
    
    for i in range(amount):
        if b_t == 'B':
            ans.append(['a', a_last_pack])
            a_last_pack+=a
        if b_t == 'R':
            ans.append(['b', b_last_pack])
            b_last_pack+=b
ans.sort(key=lambda x: (x[1], x[0]))
a_ans=[]
b_ans=[]
for idx, val in enumerate(ans):
    alpha, v = val
    if alpha == 'a':
        a_ans.append(idx+1)
    if alpha == 'b':
        b_ans.append(idx+1)

print(len(a_ans))
print(*a_ans)
print(len(b_ans))
print(*b_ans)

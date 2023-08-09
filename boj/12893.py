N, M = map(int, input().split())

chart = [i for i in range(N+1)] # 동지
enemy = [i for i in range(N+1)] # 적

def parent_find(t, chart):
    if chart[t] != t:
        chart[t] = parent_find(chart[t], chart)
    return chart[t]

def union(a, b, chart):
    parent_a = parent_find(a, chart)
    parent_b = parent_find(b, chart)
    
    if parent_a == parent_b:
        return 0

    if parent_a < parent_b:
        chart[b] = parent_a
    elif parent_b < parent_a:
        chart[a] = parent_b

ans=1
for _ in range(M):
    a, b = map(int, input().split())
    
    # 적이 존재함
    # 적에게 붙는다.
    # 아니라면 적 리스트에 오른다.
    # 적이 없음
    if parent_find(a, chart) == parent_find(b, chart):
        print(0)
        break

    if enemy[a] == a:
        # 적이 없음
        enemy[a] = b
    else:
        # 적이 존재 그러면 적의 적과 같은 집합으로 묶인다.
        union(b, enemy[a], chart)

    if enemy[b] == b:
        # 적이 없음
        enemy[b] = a
    else:
        # 적이 존재
        union(a, enemy[b], chart)
    
    #ans *= union(a, b, chart)
else:
    print(1)

# 1 3
# 2 4

#4 4
#1 2
#4 3
#2 3
#3 1

# 1   
# 2 
# 4
# 3    

# A C E
# B D 
# 

#print(ans)


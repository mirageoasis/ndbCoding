import sys
input=sys.stdin.readline

n=int(input())

row_heap=[]
col_heap=[]
for i in range(n):
    row, col = map(int, input().strip().split())
    row_heap.append((row, i+1))
    col_heap.append((col, i+1))
row_heap.sort(key=lambda x: (x[0], x[1]))
col_heap.sort(key=lambda x: (x[0], x[1]))
#print(row_heap)
#print(col_heap)
ans=0
mov_row=[]
mov_col=[]

for dest_row in range(n, 0, -1):
    # row 더해서 이동
    now_row, idx = row_heap[dest_row-1]
    if now_row == dest_row:
        continue
    mov_dir=(dest_row - now_row)//abs(dest_row - now_row)
    if mov_dir== -1:
        continue
    for i in range(n):
        if now_row == dest_row:
            break
        now_row+=mov_dir
        mov_alpha='D'
        mov_row.append((idx, mov_alpha))
        ans+=1

for dest_row in range(1, n+1):
    # row 만큼 이동
    now_row, idx = row_heap[dest_row-1]
    if now_row == dest_row:
        continue
    mov_dir=(dest_row - now_row)//abs(dest_row - now_row)
    if mov_dir== 1:
        continue
    for i in range(n):
        if now_row == dest_row:
            break
        now_row+=mov_dir
        mov_alpha='U'
        mov_row.append((idx, mov_alpha))
        ans+=1

for dest_col in range(n, 0,-1):
    # col 만큼 이동
    now_col, idx = col_heap[dest_col-1]
    if now_col == dest_col:
        continue
    mov_dir=(dest_col - now_col)//abs(dest_col - now_col)
    if mov_dir == -1:
        continue
    for i in range(n):
        if now_col == dest_col:
            break
        now_col+=mov_dir
        #mov_alpha='L'
        mov_alpha='R'
        mov_col.append((idx, mov_alpha))
        ans+=1

for dest_col in range(1, n+1):
    # col 만큼 이동
    now_col, idx = col_heap[dest_col-1]
    if now_col == dest_col:
        continue
    mov_dir=(dest_col - now_col)//abs(dest_col - now_col)
    if mov_dir == 1:
        continue
    for i in range(n):
        if now_col == dest_col:
            break
        now_col+=mov_dir
        mov_alpha='L'
        mov_col.append((idx, mov_alpha))
        ans+=1

print(ans)
for i, a in mov_row:
    print(i, a)
for i, a in mov_col:
    print(i, a)

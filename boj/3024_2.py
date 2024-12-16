# 2시 24분 시작
n=int(input())

chart=[]

for i in range(n):
    chart.append(list(input()))


def cal(start_row, start_col):
    global n, chart

    stand=chart[start_row][start_col]

    cnt=1
    for i in range(1, 3):
        new_row=start_row+i
        new_col=start_col+i
        if new_row < n and new_col < n and chart[new_row][new_col] == stand:
            cnt+=1
        else:
            break
    
    if cnt == 3:
        return True
    
    cnt=1
    for i in range(1, 3):
        new_row=start_row+i
        new_col=start_col-i
        if new_row < n and 0 <= new_col < n and chart[new_row][new_col] == stand:
            cnt+=1
        else:
            break
    
    if cnt == 3:
        return True

    cnt=1
    for i in range(1, 3):
        new_row=start_row+i
        if new_row < n and chart[new_row][start_col] == stand:
            cnt+=1
        else:
            break
    
    if cnt == 3:
        return True
    
    cnt=1
    for i in range(1, 3):
        new_col=start_col+i
        #print(new_col)
        if new_col < n and chart[start_row][new_col] == stand:
            cnt+=1
            #print(f"cnt {cnt}")
        else:
            break
    
    if cnt == 3:
        return True

    return False

flag=False
for i in range(n):
    for j in range(n):
        if chart[i][j] != '.'  and cal(i, j):
            print(chart[i][j])
            flag=True
            break
    if flag:
        break

if not flag:
    print('ongoing')
#각 칸에는 로봇

# 입력, 저장, 출력
# xx를 만족하는 출력 값들이 입력값이다.
# abs(i-a) < j - b
# b < j

# 즉, 열이 작으면서 열의 
# 로봇은 입력값들 중 최대값 저장 값으로 한다.
# 가중치를 더하면 출력값

row_len, col_len = map(int, input().split())

save_chart=[[0 for i in range(col_len)]for j in range(row_len)]
plus_chart=[]
for i in range(row_len):
    plus_chart.append(list(map(int, list(input()))))

# 출력값을 
for col in range(1, col_len):
    for row in range(row_len):
        first_row, first_col = row-1, col-1
        second_row, second_col = row, col-1
        third_row, third_col = row+1, col-1
        maxi=save_chart[second_row][second_col] + plus_chart[second_row][second_col]
        # 저장 값 + 가중치 구하기
        if 0<=first_row<row_len:
            maxi = max(maxi, save_chart[first_row][first_col] + plus_chart[first_row][first_col])
        if 0<=third_row<row_len:
            maxi = max(maxi, save_chart[third_row][third_col] + plus_chart[third_row][third_col])
        save_chart[row][col]=maxi


# 하나를 더하려면
# dp or prefix sum 

# 출력값을 저장하니까 무조껀 오른쪽으로 갈수록 커짐
# 앞열 3개의 출력 값, 
ans=0

for i in range(row_len):
    ans=max(ans, save_chart[i][col_len-1])



print(ans)
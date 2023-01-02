'''
나이트 
좌표주면 이동 가능한 경우의 수를 구한다.
'''

string = input()

row = int(string[1])
col = ord(string[0]) - ord('a') + 1

move_r = [-2, -2, 2, 2, -1, -1, 1, 1]
move_c = [-1, 1, -1, 1, -2, 2, -2, 2]

cnt = 0

for r, c in zip(move_r, move_c):
    n_row = row + r
    n_col = col + c
    if n_row < 1 or n_col < 1 or n_row > 8 or n_col > 8:
        continue
    cnt+=1

print(cnt)
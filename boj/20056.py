from math import floor
from copy import deepcopy

N, M, K = map(int, input().split())

chart = [[[] for i in range(N)] for i in range(N)]
command = []

# 7 0 1
# 6   2
# 5 4 3
# r c
move_dict = {
    0 : (-1, 0),
    1 : (-1, 1),
    2 : (0, 1),
    3 : (1, 1),
    4 : (1, 0),
    5 : (1, -1),
    6 : (0, -1),
    7 : (-1, -1),
}

for i in range(M):
    # row, col, 질량, 방향, 속력
    row, col, mass, spd, dir = map(int, input().split())
    chart[row - 1][col - 1].append([mass, spd, dir])

def loc_cal():
    new_chart = [[[] for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if len(chart[i][j]):
                for (mass, spd, dir) in chart[i][j]:
                    new_row = (i + move_dict[dir][0] * spd + N) % N
                    new_col = (j + move_dict[dir][1] * spd + N) % N
                    new_chart[new_row][new_col].append([mass, spd, dir])

    return new_chart

def new_val():
    for i in range(N):
        for j in range(N):
            if len(chart[i][j]) > 1:
                new_list = []
                mass_list = []
                dir_list = []
                cal_dir_list = []
                spd_list = []
                whole_len = len(chart[i][j])
                for (mass, spd, dir) in chart[i][j]:
                    mass_list.append(mass)
                    spd_list.append(spd)
                    dir_list.append(dir)
                
                cal_mass = floor(sum(mass_list) / 5)
                cal_vel = floor(sum(spd_list) / whole_len)
                if all(i % 2 for i in dir_list) or all(i % 2 == 0 for i in dir_list):
                    cal_dir_list = [0, 2, 4, 6]
                else:
                    cal_dir_list = [1, 3, 5, 7]
                
                for k in range(4):
                    if cal_mass > 0:
                        new_list.append([cal_mass, cal_vel, cal_dir_list[k]])
                chart[i][j] = new_list

# for i in chart:
#     print(i)
# print()

for i in range(K):
    chart = loc_cal()
    new_val()

ans = 0

for i in range(N):
    for j in range(N):
        for mass, dir, vel in chart[i][j]:
            ans += mass
            

print(ans)
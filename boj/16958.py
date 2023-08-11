import sys

INF = 99999999

N, T = map(int, sys.stdin.readline().rstrip().split())

city_list = []
city_distance_chart = [[INF for i in range(N)] for j in range(N)]

for i in range(N):
    city_list.append(tuple(map(int, sys.stdin.readline().rstrip().split())))

for i in range(N):
    for j in range(N):
        if i == j:
            city_distance_chart[i][j] = 0
        else:
            one = city_list[i]
            two = city_list[j]
            city_distance_chart[i][j] = abs(one[1] - two[1]) + abs(one[2] - two[2])

            if one[0] == 1 and two[0] == 1:
                city_distance_chart[i][j] = min(T, city_distance_chart[i][j])

for k in range(N):
    for i in range(N):
        for j in range(N):
            # 두 도시를 구한다.
            if city_distance_chart[i][j] > city_distance_chart[i][k] + city_distance_chart[k][j]:
                city_distance_chart[i][j] = city_distance_chart[i][k] + city_distance_chart[k][j]

M = int(input())

for i in range(M):
    s, d = map(int ,sys.stdin.readline().rstrip().split())
    print(city_distance_chart[s - 1][d - 1])


#print(city_pass_dict)


import itertools


N, M = list(map(int, input().split()))

chart = []

for i in range(N):
    chart.append(list(map(int, input().split())))

# 치킨 거리는 집과 가장 가까운 치킨집 사이의 거리이다.
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합이다.
# 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력한다.

# 0 은 빈칸, 1은 집 2는 치킨집

chicken = []
houses = []

def chicken_length(house ,local_chicken):
    ret = 2 * 100
    row, col = house
    for l_row, l_col in local_chicken:
        ret = min(ret, abs(l_row - row) + abs(l_col - col))
    return ret


for row in range(N):
    for col in range(N):
        if chart[row][col] == 1:
            houses.append((row, col))
        elif chart[row][col] == 2:
            chicken.append((row, col))

ans = 100000000

for local_chicken in itertools.combinations(chicken, M):
    temp = []
    for house in houses:
        temp.append(chicken_length(house, local_chicken))
    ans = min(ans, sum(temp))

print(ans)
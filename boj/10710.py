import sys

n, m = map(int, input().split())

city=[]
weather=[]
INF=1000*1000*1000*10
dp=[[INF for i in range(m+2)] for j in range(n+1)]
weather.append(0)

for i in range(n):
    city.append(int(sys.stdin.readline()))

for i in range(m):
    weather.append(int(sys.stdin.readline()))

def cal(city_num, day):
    global INF, city, weather, dp,n,m

    if dp[city_num][day] != INF:
        return dp[city_num][day]
    
    if city_num == n:
        dp[city_num][day]=0
        return 0

    # 현재 날짜
    if n - city_num > m - day + 1:
        dp[city_num][day]=INF+1
        return INF+1


    # 2가지 경우
    
    # stay....
    first=cal(city_num, day+1)

    # 도시로 이동
    second=cal(city_num+1, day+1) + weather[day] * city[city_num]
    dp[city_num][day]=min(first, second)
    return dp[city_num][day]


print(cal(0, 1))


# for d in dp:
#     print(d[1:])

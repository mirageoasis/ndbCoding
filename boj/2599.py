N=int(input())

chart = []

for i in range(3):
    a, b = list(map(int, input().split()))
    chart.append([a, b])


for i in range(chart[0][0]):
    # 출발_목표_성별
    a_b_m = i
    a_c_m = chart[0][0] - i
    b_c_m = chart[2][1] - a_c_m
    b_a_m = chart[1][0] - b_c_m
    c_a_m = chart[0][1] - b_a_m
    c_b_m = chart[2][0] - c_a_m

    if a_b_m >=0 and a_c_m >= 0 and b_c_m >= 0 and b_a_m >= 0 and c_a_m >= 0 and c_b_m >=0:
        print(1)
        print(a_b_m, a_c_m)
        print(b_a_m, b_c_m)
        print(c_a_m, c_b_m)
        break
else:
    print(0)
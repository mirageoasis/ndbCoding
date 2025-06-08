n=int(input())

li=list(map(int, input().split()))

# a 0
# b 1
# c 2
# d 3
# e 4
# f 5

# 2개 조합 작성
two_list=[(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 5), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5)]
# 3개 조합 작성
# ace, abc, abd, ade, fce, fbc, fbd, fde
three_list = [
(0, 2, 4), (0, 1, 2), (0, 1, 3), (0, 3, 4),
(5, 2, 4), (5, 1, 2), (5, 1, 3), (5, 3, 4)
]

two_min = min([li[a] + li[b] for a, b in two_list])
three_min = min([li[a] + li[b] + li[c] for a, b, c in three_list])

#print(two_min)
#print(three_min)

if n == 1:
    print(sum(li) - max(li))
elif n == 2:
    #  3개 최소 * 4
    #  2개 최소 * 4
    print(two_min * 4 + three_min * 4)
else:
    
    # 각 면 최소 * 5
    default = min(li) * ((n-2)**2) * 5

    #  사이드 기둥
    pillar = two_min * (n-1) * 4

    # 아래 변
    down = min(li) * (n-2) * 4

    # 위와 닿은 곳
    edge = three_min * 4

    # 위와 닿은변
    up = two_min * (n-2) * 4

    print(default + pillar + down + edge + up)


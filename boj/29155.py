from collections import defaultdict

N=int(input())
idx_cnt = list(map(int, input().split()))
li = []
lvl_dict = defaultdict(list)

for i in range(N):
    li.append(list(map(int, input().split())))

li.sort(key=lambda x : (x[0], x[1]))


for i in li:
    lvl_dict[i[0]].append(i[1])

#print(li)
diff = []
ans=0

#print(lvl_dict)

def sum_diff(target):
    return sum(target) + sum([abs(target[idx] - target[idx - 1]) for idx, _ in enumerate(target[1:], start=1)])

for i in range(1,5+1):
    if idx_cnt[i - 1] == len(lvl_dict[i]):
        ans+=sum_diff(lvl_dict[i])
    else: 
        # 나열 순서 (원래 숫자) (둘 간의 차이) (원래 숫자) (둘 간의 차이) (원래 숫자)
        # O D O D O D O
        # 0 1 2 3 4 5 6
        # 결론 짝수 index에서 시작 (개수 - 1) * 2
        mini = 999999999999999999
        for j in range(0, len(lvl_dict[i]) - idx_cnt[i - 1] + 1):
            mini = min(mini, sum_diff(lvl_dict[i][j:j+idx_cnt[i - 1]]))
        ans+=mini

ans+=240

print(ans)
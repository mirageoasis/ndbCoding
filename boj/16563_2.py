import math
n=int(input())
li=list(map(int, input().split()))

#print(li)
MAX=5000001
chart=[[] for i in range(MAX)]
div=[False for i in range(MAX)]

# 발상.
# 한번만 하면 괜찮으나. 여러번 하는 경우 이 경우를 저장하는 방식이 필요해 보인다.
# 앞의 결과를 활용해서 뒤의 결과를 얻는 방법을 생각해야함
# ex) 128 -> 64 * 2....
# 이러니까 소인수 분해를 하면서 해당 수에 append를 하는 방식으로 하는게?

for i in range(2, MAX):
    if not div[i]:
        for j in range(2*i, MAX, i):
            temp_j=j
            while temp_j % i == 0:
                chart[j].append(i)
                temp_j//=i
            div[j]=True
        chart[i].append(i)



for i in li:
    print(' '.join([str(j) for j in chart[i]]))
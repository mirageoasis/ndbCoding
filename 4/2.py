
'''
정수 N 이 입력된다면 해당 숫자가 0시부터 N시 59분 59초 에 몇개의 시간에 들어있나 계산

total
0 시 00분 00초 ~ 23시 59분 59초
60 * 60 * 24 = 3600 * 24 = 몇만 
5
'''

N = int(input())
cnt = 0
for i in range((N+1) * 60 * 60):
    temp = str(N)
    hour = i // 3600
    minute = i % 3600 // 60
    second = i % 60
    if temp in str(hour) or temp in str(minute) or temp in str(second):
        cnt += 1
    # 책의 해설이 애매함 왜냐하면 책은 xx시 xx분 xx초라고 했는데
    # 23 같은 경우는 22시32분32초 같은 경우는 어떻게 생각하는가?
    # 이것에 대한 해설이 써있지 않았다
print(cnt)
import sys
input=sys.stdin.readline
n, m = map(int, input().split())

# 숫자마다 개수
# count_table[0]은 무시
#print(count_table)

count_table=[(10**i - 10**(i-1)) * i for i in range(11)]
def digit_cal(m):
    global count_table
    s=0
    for i in range(1, len(count_table)):
        s+=count_table[i]
        if s >= m:
            return i 
    return -1

# 몇번째 자리인지 count
digit=digit_cal(m)

# 얘 그래서 숫자가 얼마인데?
# 10이면 
number=10**(digit-1) + (m-1 - sum(count_table[1:digit])) // digit
#print(10**(digit-1), (m - sum(count_table[1:digit])) // digit)
#print(number, digit, n)
"""
123456789
111213141516171819
"""
if number > n:
    print(-1)
else:
    temp=(m - 1 - sum(count_table[1:digit])) % digit
    #print(temp)
    string=str(number)
    print(string[temp])
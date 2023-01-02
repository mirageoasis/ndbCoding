'''
페이지 93
큰 수의 법칙
N M K
5 8 3
2 4 5 4 6 N 개
M번 더해짐 K번 초과 연속 더하기는 금지!
'''
import sys



N, M, K = map(int, sys.stdin.readline().rstrip().split())
number_list = list(map(int, sys.stdin.readline().rstrip().split()))

number_list.sort() # 정렬한다.
print(number_list)
#print(N, M, K)
s = 0

for i in range(1, M + 1):
    if not i % (K + 1): # N 번째 더할 때 
        s += number_list[-2]
    else:
        s += number_list[-1]
    #print(s)
        
print(s)
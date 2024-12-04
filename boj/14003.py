from bisect import bisect_left

n = int(input())  # 입력 크기
li = list(map(int, input().split()))  # 입력 리스트

# LIS 정보를 저장할 리스트
lis_indices = [-1] * len(li)
# LIS의 마지막 원소를 추적할 리스트
lis = [li[0]]
lis_indices[0] = 0

for idx, value in enumerate(li[1:], start=1):
    pos = bisect_left(lis, value)  # LIS 리스트에서의 위치 찾기
    if pos == len(lis):
        lis.append(value)  # 새 값을 LIS에 추가
    else:
        lis[pos] = value  # 더 작은 값으로 대체하여 최적화
    lis_indices[idx] = pos  # 현재 값의 LIS 위치 저장

# LIS의 길이를 기반으로 최적의 값 추적
cnt = len(lis)-1
result = []

for i in range(len(li) - 1, -1, -1):  # 뒤에서부터 확인
    if lis_indices[i] == cnt:  # LIS의 현재 위치와 일치
        result.append(li[i])
        cnt -= 1  # 다음 LIS 위치로 이동

# 결과 출력
print(len(result))
print(' '.join(map(str, result[::-1])))

n, k = map(int, input().split()) # N과 K를 입력 받기
a = list(map(int, input().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, input().split())) # 배열 B의 모든 원소를 입력받기

a.sort()
b.sort(reverse=True)

for i in range(n):
    if i >= k:
        break
    if a[i] < b[i]:
        a[i] = b[i]
    
print(sum(a))
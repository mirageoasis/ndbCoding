#최소한으로 바꿔라

# 문자열 10만

n, m = map(int, input().split())

first=list(map(int, list(input())))
second=list(map(int, list(input())))

first_dict=dict()
second_dict=dict()

cnt=0
for i in range(n+m):
    if first[i] == 1:
        first_dict[cnt]=i
        cnt+=1

cnt=0
for i in range(n+m):
    if second[i] == 1:
        second_dict[cnt]=i
        cnt+=1
ans=0
first_mov=0
second_mov=0
for i in range(cnt):
    a = first_dict[i]
    b = second_dict[i]
    width = abs(b-a)
    temp_first_mov = width // 2
    temp_second_mov = width // 2
    if width % 2:
        temp_first_mov+=1
    #print(width, temp_first_mov, temp_second_mov)
    first_mov+=temp_first_mov
    second_mov+=temp_second_mov
#print(first_mov, second_mov)
mid = (first_mov + second_mov) // 2
second_mid = 1 if (first_mov + second_mov) % 2 else 0

ans = mid ** 2 + (mid + second_mid) ** 2
#print(first_dict, second_dict)
print(ans)
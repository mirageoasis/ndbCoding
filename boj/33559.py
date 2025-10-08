n=int(input())
first=list(sorted(list(map(int, input().split()))))
second=list(sorted(list(map(int, input().split()))))

# 정렬
first_idx=0
second_idx=0

# heap sort 같이
first_new=[]
second_new=[]
first_left=[]
second_left=[]
cnt=0
#print(first)
#print(second)
while first_idx < n and second_idx < n:
    if first[first_idx] == second[second_idx]:
        #print(first_idx, second_idx)
        first_new.append(first[first_idx])
        second_new.append(second[second_idx])
        first_idx+=1
        second_idx+=1
        cnt+=1
    elif first[first_idx] > second[second_idx]:
        second_left.append(second[second_idx])
        second_idx+=1
    elif first[first_idx] < second[second_idx]:
        first_left.append(first[first_idx])
        first_idx+=1

while first_idx < n:
    first_left.append(first[first_idx])
    first_idx+=1

while second_idx < n:
    second_left.append(second[second_idx])
    second_idx+=1


print(cnt)
print(*(first_new + first_left))
print(*(second_new + second_left))

#$print(first_left)
#print(second_left)


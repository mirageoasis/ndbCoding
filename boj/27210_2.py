n=int(input())
li=list(map(int, input().split()))

# 1 count

one_ans=0
now_one=0
for i in li:
    if i == 2:
        if now_one > 0:
            now_one-=1
    else:
        now_one+=1
        one_ans=max(now_one, one_ans)


# 2 count
two_ans=0
now_two=0
for i in li:
    if i == 1:
        if now_two > 0:
            now_two-=1
    else:
        now_two+=1
        two_ans=max(now_two, two_ans)

print(max(two_ans, one_ans))
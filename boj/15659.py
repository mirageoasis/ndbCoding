# 후위연산

n=int(input())
nums=list(map(int, input().split()))
op=list(map(int, input().split()))

# + - * /

# -1로

new_nums = [0 for i in range(n * 2 - 1)]
# 0 2 4 6 8
for i in range(0, n):
    new_nums[i*2]=nums[i]
maxi=-100000000000000
mini=100000000000000
def postfix():
    global n, nums, op, new_nums
    stack=[]
    ret=[]
    #print(new_nums)
    for i in new_nums:
        if i <= 0:
            if not stack:
                stack.append(i)
            else:
                new_pri=abs(i) // 2
                while stack:
                    old_pri=abs(stack[-1])//2
                    if old_pri >= new_pri:
                        ret.append(stack.pop())
                    else:
                        break
                stack.append(i)
        else:
            ret.append(i)
    while stack:
        ret.append(stack.pop())
    return ret


def cal(index):
    global n, nums, op, new_nums, maxi, mini
    if index == n - 1:
        #계산
        ans_nums=postfix()
        # 0 1 / 2 3 2로 나눠서 몫찾기
        #print(ans_nums)
        ans_stack=[]
        for i in ans_nums:
            if i > 0:
                ans_stack.append(i)
            else:
                second=ans_stack.pop()
                first=ans_stack.pop()
                if i == 0:
                    ans_stack.append(first+second)
                if i == -1:
                    #print(first, second)
                    ans_stack.append(first-second)
                if i == -2:
                    ans_stack.append(first*second)
                if i == -3:
                    ans_stack.append(first//second)
                #print(ans_stack, i)
        maxi=max(maxi, ans_stack[0])
        mini=min(mini, ans_stack[0])
        #print(ans_stack[0])
        return

    for i in range(4):
        if op[i] != 0:
            new_nums[index * 2 + 1]=-i
            op[i]-=1
            cal(index+1)
            op[i]+=1
            new_nums[index * 2 + 1]=-i


cal(0)

print(maxi)
print(mini)
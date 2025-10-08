string=input()
n=int(input())
li=[]
for i in range(n):
    li.append(input().strip())

# chart
# -1 은 아직 정해지지 않음. 1은 됨. 0은 안됨

dp=[-1 for i in range(len(string)+1)]
dp[len(string)]=1

def cal(index):
    global dp, li, string, li
    if dp[index] != -1:
        return dp[index]
    # 하나라도 성공하면 1 으로 마킹한다.
    ans=0
    for i in li:
        if index + len(i) <= len(string):
            new_str=string[index:index+len(i)]
            if new_str == i:
                ans |= cal(index+len(i))
    
    dp[index]=ans
    return dp[index]

print(cal(0))

#print(dp)
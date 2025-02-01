# 그리디 아니면 dp 부르트는 가능한가?

'''
문자열 길이 최대 25
'''
t=int(input())
ans=0
def dfs(string):
    global ans
    #print(string)
    if len(string) == 0:
        ans=1
        return
    if len(string) == 1:
        return
    idx=0
    for i in range(1, len(string)):
        if string[i] != string[idx]:
            if i - idx > 1:
                dfs(string[:idx] + string[i:])
            idx=i
    #print(string)
    # 다 같으면 ans+=1
    if idx == 0:
        ans=1



for _ in range(t):
    s=input()
    ans=0
    dfs(s)
    print(ans)
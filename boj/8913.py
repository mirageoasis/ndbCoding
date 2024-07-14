N=int(input())


ans=0

def dfs(string):
    #print(string)
    global ans
    if len(string) == 0:
        ans+=1
        return
    if len(string) == 1:
        return
    
    # 이어진 문자열 목록 찾기
    idx=0
    for i in range(1, len(string)):
        if string[i] != string[idx]:
            if i - idx > 1:
                dfs(string[:idx] + string[i:])
            idx=i
    #print(string)
    # 다 같으면 ans+=1
    if idx == 0:
        ans+=1


for _ in range(N):
    string=input()
    # 오른쪽에서 탐색하면서 1개의 문자열만 가지고 있는 친구를 찾는다.
    ans=0
    dfs(string)
    if ans:
        print(1)
    else:
        print(0)

"""
음... 일단 
시간복잡도를 12!이라고 생각했는데

가지치기가 되면서 12!이 나오지 않는다. 그래서 브루트포스로 풀 수 있다...
"""

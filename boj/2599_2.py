n=int(input())

li=[]

for i in range(3):
    li.append(list(map(int, input().split())))


#ans
# a남 b녀, a남 c녀
# b남 a녀, b남 c녀
# c남 a녀, c남 b녀
ans=[[0, 0], [0, 0], [0, 0]]

flag=False

def ansable(ans):
    for i in range(3):
        if ans[i][0] < 0:
            return False
        if ans[i][1] < 0:
            return False
    return True

for i in range(li[0][0]+1):
    # a남 b녀
    
    ans[0][0]=i # a남 b녀
    ans[0][1]=li[0][0] - ans[0][0] # a남 - a남 b녀 -> a남 c녀

    ans[1][1]=li[2][1] - ans[0][1] # c녀 - a남 c녀 -> b남 c녀
    ans[1][0]=li[1][0] - ans[1][1] # b남 - b남 c녀 -> b남 a녀

    ans[2][0]=li[0][1] - ans[1][0] # a녀 - b남 a녀 -> c남 a녀
    ans[2][1]=li[2][0] - ans[2][0] # c남 - c남 a녀 -> c남 b녀

    if ansable(ans):
        flag=True
        break

if not flag:
    print(0)
else:
    print(1)
    for i in range(3):
        print(ans[i][0], ans[i][1])
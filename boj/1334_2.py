# 일단 생각을 해보자
# 가운데가 1순위다. 만약에 아니라면 앞으로 가고 0으로 만든다.
# 12921
# 13031
# 짝수 일 때 문제
# 1899
n=input()

def nine(n_list):
    # 0 1 2 3
    for i in range(len(n_list)//2):
        if n_list[i] != 9:
            return False
    return True

n_list=[int(i) for i in list(n)]
#홀수
if len(n) % 2:
    n_list.insert(0, 0)
    mid=len(n_list)//2
    for i in range(mid,-1,-1):
        n_list[i]+=1
        n_list[i]%=10
        if n_list[i]:
            break
    if n_list[0] == 0:
        n_list=n_list[1:]
else:
    
    left_mid=len(n_list)//2-1
    right_mid=len(n_list)//2
    if n_list[left_mid] <= n_list[right_mid]:
        if nine(n_list):
            n_list=[1] + [0 for i in range(len(n_list))] 
        else:
        #덧셈
            for i in range(left_mid,-1,-1):
                n_list[i]+=1
                n_list[i]%=10
                if n_list[i]:
                    break

"""
125721 -> 5에 6을 더하기

127521 -> 7과 동일하게 만든다.
"""

#print(n_list)
ans=""
if len(n_list) % 2 == 0:
    left_mid=len(n_list)//2-1
    for i in range(len(n_list)//2):
        ans+=str(n_list[i])
    ans+=ans[::-1]
else:
    for i in range(len(n_list)//2):
        ans+=str(n_list[i])
    rever_ans=ans[::-1]
    mid=str(n_list[len(n_list)//2])
    ans+=mid
    ans+=rever_ans

print(ans)
from collections import Counter

origin=list(input())
n=int(input())
li=[]
li_counter=[]
dp=[]
for i in range(n):
    string=input()
    li.append(string)

#print(li_counter)
#print(origin_counter)

INF=999999999

dp=[INF for i in range(len(origin))]
#print(dp)


# x번 index부터 시작한 string의 값
string_val=[[INF for i in range(len(origin))] for j in range(len(li))]
li.sort(key=lambda x: len(x))

for i in range(len(li)):
    li_elem = li[i]
    for j in range(len(origin)):
        origin_bit=[0 for i in range(26)]
        li_bit=[0 for i in range(26)]
        start_idx=j
        end_idx=j+len(li_elem)
        if end_idx > len(origin):
            break
        cnt=0
        for k in range(start_idx, end_idx):
            if origin[k] != li_elem[k-start_idx]:
                cnt+=1
                origin_bit[ord(origin[k]) - ord('a')]+=1
                li_bit[ord(li_elem[k-start_idx]) - ord('a')]+=1
        flag=True
        for t in range(26):
            if origin_bit[t] != li_bit[t]:
                flag=False
        if flag:
            string_val[i][j]=cnt

# for c in string_val:
#     print(c)

def cal(idx):
    global INF, dp, string_val
    #print(idx)
    if idx == -1:
        dp[idx]=0
        return dp[idx]
    if dp[idx] != INF:
        return dp[idx]
    
    ret=INF+1
    for i in range(len(li)):
        start_idx=idx-len(li[i])+1
        if start_idx >= 0:
            if string_val[i][start_idx] < INF:
                ret = min(ret, string_val[i][start_idx]+cal(start_idx-1))

    dp[idx]=ret
    return dp[idx]

ans=cal(len(origin) - 1)
#print()
#print(dp)
print(ans if ans < INF else -1)
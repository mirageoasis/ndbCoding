start, end = map(int, input().split())


#num까지 1 포함
def from_bin(num):
    if num ==0:
        return 0
    elif num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4

    ans=0
    num_bin=bin(num)[2:] # 이진수 문자열
    num_len=len(num_bin) # 이진수 문자열 길이
    
    for idx in range(num_len-1):
        later=int(num_bin[idx+1:] if num_bin[idx+1:] else "0", 2) + 1
        now_cnt=2**(num_len-idx-1) # 한 주기 마치면 얻는 1의 수
        period_cnt=(num+1)//(now_cnt*2) # 주기의 수
        #print(period_cnt, now_cnt, period_cnt * now_cnt, (later if num_bin[idx] == "1" else 0))
        # 1111 같이 주기를 다 돈 것과 중간에 끊기는 것을 둘다 계산하면 안되니까 식에다 넣어준다.
        ans+=period_cnt * now_cnt + (later if num_bin[idx] == "1" and later != now_cnt else 0)
        #print(ans)
    
    ans+=(num+1)//2

    return ans

print(from_bin(end) - from_bin(start-1))
#print(from_bin(start))
# print(2)
# print(from_bin(2))
# print()
# print(12)
# print(from_bin(12))
# print()
# print(13)
# print(from_bin(13))
# print()
# print(14)
# print(from_bin(14))
# print()
# print(15)
# print(from_bin(15))
# 순서가 있고
from collections import defaultdict
n, m = map(int, input().split())
li = list(map(int, input().split()))

# 콘센트가 차지 않았다면 별상관 ㄴ
# 하지만 다 찼다면? 제일 사용 안되는 친구 교체
s=set()
ans=0
for i in range(len(li)):
    now=li[i]
    if now not in s:
        if len(s) < n:
            s.add(now)
        else:
            # 제일 사용 안되는 친구 ㄱ
            rm=now
            rng=0
            for a in s:
                temp_rng=101
                for j in range(i+1, len(li)):
                    if li[j] == a:
                        temp_rng=j-i
                        break
                if temp_rng > rng:
                    rng=temp_rng
                    rm=a
            s.remove(rm)
            s.add(now)

            ans+=1
print(ans)
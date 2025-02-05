import sys
input=sys.stdin.readline

x,y,w,s=map(int, input().split())

if w * 2 < s:
    print((x+y)*w)
else:
    mini=min(x,y)
    maxi=max(x,y)-min(x,y)
    ans=mini*s
    # 만약에 대각선이 일반 이동보다 좋다면 최대한 활용
    if s < w:
        # 2좌표씩 대각선으로 이동
        ans+=maxi//2*2*s
        ans+=maxi%2*w
    else:
        ans+=maxi*w
    print(ans)

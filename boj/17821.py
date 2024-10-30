# 5시 시작
from itertools import permutations

N=int(input())
chart=[]

for i in range(N):
    li=list(map(int, input().split()))
    li.insert(0, 0)
    chart.append(li)

#print(chart)

ans=0
number=[2,3,4,5,6,7,8,9]
def game(batter_record):
    global N, ans
    
    final_score=0
    inning=0
    batter_record_idx=0
    while inning < N:
        # inning_chart는 현재 이닝의 선수들 타석 정보
        inning_chart=chart[inning]
        # 현재 이닝에서 기록한 점수
        inning_score=0
        # record 기준으로 분석한다.
        out_cnt=0
        base=[0, 0, 0]
        while out_cnt < 3:
            # x번 타자
            player=batter_record[batter_record_idx]
            result=inning_chart[player]

            if result == 0:
                out_cnt+=1
            elif result == 4:
                inning_score+=(base[0]+base[1]+base[2]+1)
                base[0], base[1], base[2] = (0, 0, 0)
            elif result == 3:
                inning_score+=(base[2]+base[1]+base[0])
                base[2]=1
                base[0], base[1] = (0, 0)
            elif result == 2:
                inning_score+=(base[2]+base[1])
                base[2]=base[0]
                base[1]=1
                base[0]=0
            elif result == 1:
                inning_score+=base[2]
                base[2]=base[1]
                base[1]=base[0]
                base[0]=1
            
            batter_record_idx+=1
            batter_record_idx%=9

        
        final_score+=inning_score
        inning+=1

    ans=max(final_score, ans)

for i in permutations(number, r=8):
    i=list(i)
    i.insert(3, 1)
    game(i)

print(ans)
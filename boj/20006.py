# 방 없으면 새로 생성
# 입장 가능하면 먼저 생성된 곳에 입장
# 처음 입장한 플레이어 기준 -+ 10
# 차면 게임 시작~

def room_finder(room, limit, level, name):
    # 아예 없으면 추가
    if not room:
        room.append([(level, name)])
        return
    
    for i in room:
        # 돌면서 찾는다.
        if len(i) < limit and level in range(i[0][0] - 10, i[0][0] + 11):
            i.append((level, name))
            break
    else:
        room.append([(level, name)])


p, m = map(int, input().split())
room = []

for _ in range(p):
    a, b = input().split()
    room_finder(room, m,int(a), b)

for i in room:
    t = sorted(i, key=lambda x: x[1])
    if len(t) == m:
        print("Started!")
    else:
        print("Waiting!")
    for j in t:
        print(j[0], j[1])
from collections import deque

# 상태
HORIZONTOL=0
VERTICAL=1

# 가로인 상태 -> col 좌표 쁠마 1 / 회전 4가지 
# 세로인 상태 -> row 좌표 쁠마 1 / 회전 4가지

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def check(cor1, cor2, new_board):
    if new_board[cor1[0]][cor1[1]] == 1:
        #print(cor1[0], cor1[1], 1)
        return False
    if new_board[cor2[0]][cor2[1]] == 1:
        #print(cor2[0], cor2[1], 2)
        return False
    return True


def bfs(new_board):
    q = deque()
    # ((좌표) (좌표) 현재 방향) (가격)

    fin_cord = len(new_board) - 2

    q.append((((1,1), (1,2), HORIZONTOL), 0))
    
    while q:
        # 확인절차 생략
        state, cost = q.popleft()
        cor1, cor2, pos = state # 좌표1, 좌표2, 현재 상태
        #print(state, cost)
        if (cor1[0] == fin_cord and cor1[1] == fin_cord) or (cor2[0] == fin_cord and cor2[1] == fin_cord):
            return cost
        
        # 회전
        if pos == HORIZONTOL:
            #up
            #print(cor1[1] + 1, cor2[1] + 1, 42)
            if new_board[cor1[0]][cor1[1] + 1] == 0 and new_board[cor2[0]][cor2[1] + 1] == 0:
                # 회전 실시
                # 좌
                q.append(((cor1, (cor1[0], cor1[1] + 1), VERTICAL), cost+1))
                # 우
                q.append((((cor2[0], cor2[1] + 1), cor2, VERTICAL), cost+1))

            #down
            if new_board[cor1[0]][cor1[1] - 1] == 0 and new_board[cor2[0]][cor2[1] - 1] == 0:
                # 좌
                q.append(((cor1, (cor1[0], cor1[1] - 1), VERTICAL), cost+1))
                # 우
                q.append((((cor2[0], cor2[1] - 1), cor2, VERTICAL), cost+1))
                
        elif pos == VERTICAL:
            #right
            if new_board[cor1[0] + 1][cor1[1]] == 0 and new_board[cor2[0] + 1][cor2[1]] == 0:
                # 회전 실시
                q.append(((cor1, (cor1[0] + 1, cor1[1]), HORIZONTOL), cost+1))
                # 우
                q.append((((cor2[0] + 1, cor2[1]), cor2, HORIZONTOL), cost+1))

            #left
            if new_board[cor1[0] - 1][cor1[1]] == 0 and new_board[cor2[0] - 1][cor2[1]] == 0:
                # 회전 실시
                q.append(((cor1, (cor1[0] - 1, cor1[1]), HORIZONTOL), cost+1))
                # 우
                q.append((((cor2[0] - 1, cor2[1]), cor2, HORIZONTOL), cost+1))
            
        else:
            print("error")


        # 이동
        for i in range(0, 4):
            if check((cor1[0] + dx[i], cor1[1] + dy[i]), (cor2[0] + dx[i], cor2[1] + dy[i]), new_board):
                q.append((((cor1[0] + dx[i], cor1[1] + dy[i]), (cor2[0] + dx[i], cor2[1] + dy[i]), pos), cost+1))
        
def solution(board):
    answer = 0

    new_board = [[1 for i in range(len(board) + 2)] for j in range(len(board) + 2)]
    
    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i+1][j+1] = board[i][j]
    # -2

    answer = bfs(new_board)
    print(answer)

    #for _ in new_board:
    #    print(_)

    return answer

solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]])
'''
build_frame의 원소는 [x, y, a, b]형태입니다.
x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
바닥에 보를 설치 하는 경우는 없습니다.

최종 구조물의 상태는 아래 규칙에 맞춰 return 해주세요.
return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고있어야 합니다.
return 하는 배열의 원소는 [x, y, a] 형식입니다.
x, y는 기둥, 보의 교차점 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
기둥, 보는 교차점 좌표를 기준으로 오른쪽, 또는 위쪽 방향으로 설치되어 있음을 나타냅니다.
a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
return 하는 배열은 x좌표 기준으로 오름차순 정렬하며, x좌표가 같을 경우 y좌표 기준으로 오름차순 정렬해주세요.
x, y좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다
'''

'''
코드로 보는 기둥 설치
# 좌표가 0인 경우 -> 좌표 0인지 점검
# 아래가 기둥인 경우 -> row -1 좌표가 기둥인지 점검 --
# 아래가 보인 경우 -> col -1 좌표가 보인지 점검 

코드로 보는 보 설치
# 양 옆이 보인 경우 -> -1 + 1 col 점검
# 자신이 있는 곳 아래가 기둥인 경우 -> row -1 점검
# 자신이 있는 곳 오른쪽 아래가 기둥인 경우 -> col +1 row -1 점검

코드로 보는 기둥 철거
# 자신 위에 기둥이 존재하면 절대 안된다.
# 자신 위에 보가 존재할 때 그 

코드로 보는 보 제거

# 오른쪽 끝

'''
## 일단 시간 복잡도 되는지 계산하기

# 기둥
            # (0, -1) 에 기둥 존재
            # (0, -1) 보 존재 
            # (-1, -1) 보 존재
            # 좌표 0
# 보
            # (0, -1) 기둥 존재 
            # (1, -1) 기둥 존재
            # (-1, 0) / (1, 0) 보 존재
import time

def pass_install(answer, x, y, kind):
    if kind == 0:
        # 기둥
        if y == 0:
            return True
        elif [x, y - 1, 0] in answer:
            return True
        elif [x, y, 1] in answer or [x - 1, y, 1] in answer:
            return True
    else:
        if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
            return True
        elif [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
            return True
    
    return False

def solution(n, build_frame):
    answer = []
    
    for x, y, kind, install in build_frame:
        if install:
            if pass_install(answer, x, y, kind):
                answer.append([x, y, kind])
        else:
            answer.remove([x, y, kind])
            for a, b, k in answer:
                if not pass_install(answer, a, b, k):
                    answer.append([x, y, kind])
                    break
            
    answer.sort(key = lambda x : (x[0], x[1], x[2]))

    return answer

print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
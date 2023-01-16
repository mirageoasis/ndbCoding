def check_out(padded_lock, m, n):
    for i in range(n):
        for j in range(n):
            if not padded_lock[i+m][j+m]:
                return False
    return True
    
def check_in(padded_lock, key, m, n, i, j):
    for x in range(m):
        for y in range(m):
            if key[x][y] == 1:
                if padded_lock[x+i][y+j] == 1:
                    return False
                else:
                    padded_lock[x+i][y+j] = 1
    return True


def solution(key, lock):
    answer = False
    
    m = len(key)
    n = len(lock)    
    
    for _ in range(4):
        
        
        for i in range(0, m + n):
            for j in range(0, m + n):
                # padded lock 초기화
                padded_lock=[[0 for i in range(2 * m + n)] for i in range(2 * m + n)]
                for x in range(n):
                    for y in range(n):
                        padded_lock[m+x][m+y]=lock[x][y]

                if check_in(padded_lock, key,m, n, i, j):
                    if check_out(padded_lock, m, n):        
                        answer=True
        
        new_key = [[0 for i in range(m)] for j in range(m)]
        for i in range(m):
            for j in range(m):
                new_key[m - j - 1][i] = key[i][j]
        key=new_key
        
        
# 배열은 한 줄 단위로 생각해도 ㄱㅊ다.
    
    return answer
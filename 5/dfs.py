
# 인접 행렬을 활용한 dfs

def dfs(graph, visited, point):

    stack = []
    stack.append(point)
    visited[point] = True
    print(point)
    while stack:    
        for i in graph[stack[-1]]:
            if not visited[i]:
                print(i)
                visited[i] = True
                stack.append(i)
                break
        else:
            stack.pop()
        

    


def main():
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7]
    ]
    
    # 9개
    visited = [False] * 9

    dfs(graph, visited, 1)


main()



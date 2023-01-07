from collections import deque


def bfs(graph, visited, point):
    q = deque()
    
    q.append(point)
    
    while q:
        now = q.popleft()
        #if visited[now]:
            #continue
        
        print(now)
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)




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

    bfs(graph, visited, 1)

main()
from collections import deque
n, m = map(int, input().split())

# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

graph = []
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    graph.append(list(map(int, input())))


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        tmp = graph[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <=-1 or nx >=n or ny <= -1 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = tmp+1


bfs(0,0)

for i in range(n):
    print(graph[i])


print(graph[n-1][m-1])
from collections import deque

n, m = map(int,input().split())

map = [list(map(int,input())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs():
    queue = deque()
    queue.append((0,0))
    visited[0][0] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and map[nx][ny]==1:
                visited[nx][ny] = True
                map[nx][ny] = map[x][y] + 1
                queue.append((nx,ny))


bfs()
print(map[n-1][m-1])




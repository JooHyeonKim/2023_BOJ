from collections import deque
n, m = map(int, input().split())
maze =[]
for _ in range(n):
    maze.append(list(input().rstrip()))


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(i,j):

    queue = deque()
    queue.append((i,j))
    dist = [[0] * m for _ in range(n)]
    max_d = 0

    while queue:
        x, y = queue.popleft()
        if max_d < dist[x][y]:
            max_d = dist[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue

            elif 0<=nx<n and 0<=ny<m and dist[nx][ny]==0 and maze[nx][ny]=='L':
                dist[nx][ny] = dist[x][y]+1
                queue.append((nx,ny))

    return max_d

max_dist=0
for i in range(n):
    for j in range(m):
        if maze[i][j]=='L':
            tmp = bfs(i,j)
            if max_dist < tmp:
                max_dist = tmp

print(max_dist)


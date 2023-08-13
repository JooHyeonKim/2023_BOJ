import sys
from collections import deque

n, m = map(int, input().split())
input = sys.stdin.readline
maze =[list(input()) for _ in range(n)]


dx = [1,-1,0,0]
dy = [0,0,1,-1]
def bfs(i,j):
    dist = [[0] * m for _ in range(n)]
    queue = deque()
    queue.append((i,j))
    dist[i][j] = 1

    max_d = 0

    while queue:
        x, y = queue.popleft()
        max_d = max(max_d, dist[x][y])

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
            max_dist = max(max_dist,bfs(i,j))

print(max_dist-1)


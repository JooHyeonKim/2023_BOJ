import sys
from collections import deque

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            nx = (nx+n)%n
            ny = (ny+m)%m

            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                queue.append((nx, ny))




cnt = 0

def show():
    for g in graph:
        print(g)

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            cnt += 1
            bfs(i, j)

print(cnt)
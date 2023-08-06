import sys
from collections import deque
input = sys.stdin.readline

m, n = map(int, input().split())
day = 0
#0 : 익지 않은 토마토
#1 : 익은 토마토

toma = [list(map(int, input().split())) for _ in range(n)]

d=1

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def bfs():
    global d
    queue = deque()

    for i in range(n):
        for j in range(m):
            if toma[i][j] == 1:
                queue.append((i, j))


    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if toma[nx][ny] == 0:
                toma[nx][ny] = toma[x][y] + 1
                if toma[x][y] + 1 > d:
                    d = toma[x][y] + 1
                queue.append((nx,ny))


bfs()

for i in range(n):
    if 0 in toma[i]:
        d= 0
        break


print(d-1)
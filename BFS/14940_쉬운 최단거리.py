from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
visit = [[False]*m for _ in range(n)]

a=0
b=0

graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:      # 목표지점을 입력받으면 인덱스 저장
            a = i
            b = j
            break

visit[a][b] = True   # 목표지점 방문처리
graph[a][b] = 0      # 목표지점을 0으로 설정

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(a, b):
    queue = deque()
    queue.append((a,b))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m or graph[nx][ny] == 0:
                continue

            if not visit[nx][ny]:
                graph[nx][ny] = graph[x][y] + 1
                visit[nx][ny] = True
                queue.append((nx, ny))

dfs(a, b)

for i in range(n):
    for j in range(m):
        if not visit[i][j] and graph[i][j] == 1:
            print(-1, end = ' ')
        else:
            print(graph[i][j], end=' ')

    print()

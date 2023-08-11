from collections import deque

n = int(input())
color = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    words = input()
    li = []
    for w in words:
        li.append(w)
    color.append(li)

def bfs(i,j):
    queue = deque()
    queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <n and 0 <= ny <n and not visited[nx][ny] and color[x][y]==color[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx,ny))

def pnt():
    for v in visited:
        print(v)

visited = [[False]*n for _ in range(n)]
res1 = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i,j)
            res1 += 1



for i in range(n):
    for j in range(n):
        if color[i][j] == 'R':
            color[i][j] = 'G'

visited = [[False]*n for _ in range(n)]
res2 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            bfs(i,j)
            res2 += 1

print(res1, res2)

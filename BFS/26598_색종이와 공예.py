import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

graph = []

for _ in range(n):
    word = input()
    lst = []
    for w in word:
        lst.append(w)
    graph.append(lst)

visited = [[-1]*m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0 # 탐색한 칸 개수

def bfs(i, j):
    global cnt
    queue = deque()
    queue.append((i,j))
    visited[i][j] = 1
    min_x = i
    min_y = j
    mx = i
    my = j

    while queue:
        x, y = queue.popleft()
        if x < min_x : min_x = x
        if y < min_y : min_y = y

        if x > mx : mx = x
        if y > my : my = y
        cnt += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >=m or visited[nx][ny]!= -1:
                continue

            if graph[x][y] == graph[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return min_x, min_y, mx, my # 끝 점

result = "dd"


check = True
for i in range(n):
    for j in range(m):

        if visited[i][j] == -1:
            cnt=0
            a1, b1, a2, b2 = bfs(i,j)
            length = b2-b1+1
            height = a2-a1+1
            #print('cnt = ', cnt, ' 넓이 = ', length*height)

            if length*height != cnt:
                result = "BaboBabo"
                check = False
                break
    if not check:
        break

print(result)





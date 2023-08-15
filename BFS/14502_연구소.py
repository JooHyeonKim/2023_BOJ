import copy
from collections import deque
import sys
import copy

input = sys.stdin.readline

n, m = map(int, input().split())
real_map = [list(map(int,input().split())) for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

res = -1 #안전구역 개수
def bfs():
    queue = deque()
    map = copy.deepcopy(real_map)

    for i in range(n):
        for j in range(m):
            if map[i][j] == 2:
                queue.append((i,j))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            elif map[nx][ny] == 0:
                map[nx][ny] = 2
                queue.append((nx, ny))

    tmp = 0
    for i in range(n):
        for j in range(m):
            if map[i][j] == 0:
                tmp += 1

    global res
    res = max(res, tmp)

    # for ma in map:
    #     print(ma)
    # print()

def make_wall(cnt):
    if cnt == 3:
        bfs()
        return

    for i in range(n):
        for j in range(m):
            if real_map[i][j] == 0:
                real_map[i][j] = 1
                make_wall(cnt+1)
                real_map[i][j] = 0

make_wall(0)
print(res)


import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n+1):
    graph[i].sort()
    print(graph[i])

visited = [False]*(n+1)
def bfs():
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        x = queue.popleft()
        print(x, end = ' ')
        for nx in graph[x]:
            if not visited[nx]:
                queue.append(nx)
                visited[nx] = True


bfs()
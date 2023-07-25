from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]
answer = [0]*(n+1)   #답을 저장할 배열

for i in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


def bfs(graph, v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                answer[i] = x
                visited[i] = True
                queue.append(i)


bfs(graph, 1, visited)
for i in range(2, n+1):
    print(answer[i])
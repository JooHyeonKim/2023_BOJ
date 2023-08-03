import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
visited = [False]*(n+1)    # 방문 여부 표시
l = [0]*(n+1)  # 루트로 부터의 거리
graph = [[] for i in range(n+1)]

for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs():

    queue = deque()
    visited[1] = True #루트노드 방문처리
    queue.append(1)     # 루트노드 큐에 삽입
    l[1] = 0

    while queue:
        x = queue.popleft()          #큐에서 하나 pop
        for i in graph[x]:          # pop한 노드의 주변노드 중에서
            if not visited[i]:       # 아직 방문 안한것들
                queue.append(i)     # 큐에 추가
                visited[i] = True   # 방문처리
                l[i] = l[x]+1       # 주변노드 거리 = 현재노드 거리 + 1


bfs()

for i in range(2, n+1):

    if len(graph[i]) == 1:
        min = graph[i][0]
    else:
        min = graph[i][0]
        t = l[min]

        for j in graph[i]:
            if t > l[j]:
                t = l[j]
                min = j

    print(min)

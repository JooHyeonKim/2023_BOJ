from collections import deque

n, k = map(int, input().split())
max = 100001
cnt = 0
dist = [0] * max
visited = [False] * max
def dfs():

    queue = deque()
    queue.append(n)
    visited[n] = True

    global cnt

    while queue:
        x = queue.popleft()

        if x == k:
            cnt += 1
            continue

        for nx in (2*x, x+1, x-1):
            if 0 <= nx < max and (not visited[nx] or dist[nx] == dist[x]+1):
                visited[nx] = True
                queue.append(nx)
                dist[nx] = dist[x] + 1


dfs()

print(dist[k])
print(cnt)


from collections import deque

n, k = map(int, input().split())

max = 100001
visited = [False]*max
dist = [0]*max
check = [0]*max
path = []
def move():
    t = k
    path.append(k)

    for _ in range(dist[k]):
        next = check[t]
        path.append(next)
        t = next


def bfs():
    queue = deque()

    queue.append(n)
    visited[n] = True

    while queue:
        x = queue.popleft()
        if x == k:
            move()
            break

        for nx in (2*x, x-1, x+1):
            if 0 <= nx < max and not visited[nx]:
                dist[nx] = dist[x] + 1
                check[nx] = x
                visited[nx] = True
                queue.append(nx)

bfs()
print(dist[k])
path.reverse()
for p in path:
    print(p, end=' ')

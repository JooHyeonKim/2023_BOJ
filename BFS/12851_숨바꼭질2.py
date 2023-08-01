from collections import deque

n, k = map(int, input().split())
max = 100001
cnt = 0
dist = [0] * max
visited = [False] * max
def dfs():

    queue = deque()
    queue.append(n)
    global cnt

    while queue:

        x = queue.popleft()
        if x == k and min == dist[x]:
            cnt += 1

        if 2*x < max and not visited[2*x]:
            dist[2*x] = dist[x] + 1

            if 2*x == k:
                min = dist[2*x]
            else:
                visited[2 * x] = True

            queue.append(2*x)

        if  x+1 < max and visited[x+1]:
            dist[x+1] = dist[x] + 1
            if x+1 == k:
                min = dist[x+1]
            else:
                visited[x+1] = True
            queue.append(x+1)

        if x-1 >= 0 and not visited[x-1]:
            dist[x-1] = dist[x] + 1
            if x-1 == k:
                min = dist[x-1]
            else:
                visited[x - 1] = True
            queue.append(x-1)


dfs()
print(dist[k])
print(cnt)


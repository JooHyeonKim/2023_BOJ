from collections import deque

n, k = map(int, input().split())

max = 100001

dist = [0]*max
visited = [False]*max

queue = deque()
queue.append(n)
visited[n] = True

def dfs():

    while queue:
        x = queue.popleft()
        if x == k:
            return

        if 2 * x < max and not visited[2 * x]:
            t = 2 * x
            dist[t] = dist[x]
            visited[t] = True
            queue.append(t)

        if (x - 1) >= 0 and not visited[x - 1]:
            t = x - 1
            dist[t] = dist[x] + 1
            visited[t] = True
            queue.append(t)

        if (x + 1) >= 0 and not visited[x + 1]:
            t = x + 1
            dist[t] = dist[x] + 1
            visited[t] = True
            queue.append(t)

dfs()

print(dist[k])
# for i in range(1, k+1):
#     print(i, '까지의 길이 : ', dist[i])
# print()

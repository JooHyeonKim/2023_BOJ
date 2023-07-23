n, m = map(int, input().split())
cnt = 0

graph = []
for i in range(n):
    graph.append(list(map(int, input())))


def dfs(i, j):

    if i <= -1 or i >= n or j <= -1 or j >= m:
        return False

    if graph[i][j] == 0:

        graph[i][j] = 1
        dfs(i, j-1)  # 왼쪽
        dfs(i-1, j)  # 위쪽
        dfs(i, j + 1)  # 오른쪽
        dfs(i+1, j)  # 아래

        for i in range(n):
            print(graph[i])
        print()
        return True

    return False



for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            cnt+=1

print(cnt)
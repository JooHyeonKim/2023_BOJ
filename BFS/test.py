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


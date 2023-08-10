import sys
import heapq

input = sys.stdin.readline

n = int(input())
meet = []

for _ in range(n):
    s, e = map(int, input().split())
    meet.append([s,e])

meet.sort(key=lambda x: x[0])

h = [0]
cnt = 1

for s, e in meet:
    if s >= h[0]:
        heapq.heappop(h)
    else:
        cnt += 1

    heapq.heappush(h, e)

print(cnt)
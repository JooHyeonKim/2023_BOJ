import heapq
import sys

n = int(input())

card = []
input = sys.stdin.readline

for _ in range(n):
    heapq.heappush(card, int(input()))


if n == 1:
    print(0)

else:

    tmp1 = heapq.heappop(card)
    sum = 0

    while len(card) >= 1:
        tmp2 = tmp1 + heapq.heappop(card)
        tmp1 = tmp2

        sum += tmp2

    print(sum)






import sys

input = sys.stdin.readline

n = int(input())
apart = [[0]*15 for _ in range(15)]

for i in range(15):
    apart[0][i] = i


def DP(a, b): #a층 b호
    for i in range(1, a+1):
        tmp = 0

        for j in range(1, b+1):

            tmp += apart[i-1][j]

            if apart[i][j] == 0:
                apart[i][j] = tmp



for _ in range(n):
    k = int(input())
    n = int(input())
    DP(k, n)

    print(apart[k][n])



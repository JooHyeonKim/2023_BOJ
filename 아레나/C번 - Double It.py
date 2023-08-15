import sys

input = sys.stdin.readline

n = int(input())

num = list(map(int,input().split()))


M = max(num)
m = min(num)
res = M-m

for i in range(n):
    num[i]*=2
    M = max(num)
    m = min(num)
    res = min(res, M-m)

print(res)

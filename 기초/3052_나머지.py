import sys

input = sys.stdin.readline

r = [] # 나머지들

for _ in range(10):
    n = int(input())
    r.append(n%42)

r2 = set(r)
print(len(r2))
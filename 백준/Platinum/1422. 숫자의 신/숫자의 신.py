import sys

k, n = map(int, input().split())
num = []
result = []
M = -1
for _ in range(k):
    t = input()
    num.append(t)
    M = max(int(t), M)

for _ in range(n-k):
    num.append(str(M))

num.sort(key=lambda x : x*10, reverse = True)

res = ''.join(num)

print(int(res))
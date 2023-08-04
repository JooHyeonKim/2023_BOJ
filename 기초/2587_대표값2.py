import sys

input = sys.stdin.readline
li = []
sum = 0

for _ in range(5):
    x = int(input())
    li.append(x)
    sum += x

li.sort()
print(sum//5)
print(li[2])

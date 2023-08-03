import sys

input = sys.stdin.readline
list = []

n = int(input())
for i in range(n):
    age, name = input().split()
    list.append([int(age), i, name])

list.sort()

for i in range(n):
    print(list[i][0], list[i][2])
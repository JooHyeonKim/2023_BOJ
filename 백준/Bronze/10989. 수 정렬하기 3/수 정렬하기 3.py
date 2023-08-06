import sys

input = sys.stdin.readline

max = 10001
n = int(input())
num = [0]*max

for _ in range(n):
    num[int(input())] += 1

for i in range(max):
    for _ in range(num[i]):
        print(i)



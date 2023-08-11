import sys

input = sys.stdin.readline

n = int(input())

arr = set(map(int, input().split()))

m = int(input())

find = list(map(int,input().split()))

for f in find:
    if f in arr:
        print("1")
    else:
        print(0)
import sys

input = sys.stdin.readline

n = int(input())

def score(li):
    add = 1
    s=0
    for l in li:
        if l == 'O':
            s += add
            add += 1
        elif l == 'X':
            add = 1

    return s



for _ in range(n):
    ox = list(input())
    res = score(ox)
    print(res)



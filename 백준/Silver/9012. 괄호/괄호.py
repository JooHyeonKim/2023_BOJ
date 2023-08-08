import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    result = "YES"

    stack = []
    data = input()

    for d in data:
        if d =='(':
            stack.append(d)
        if d== ')':
            if len(stack) == 0:
                result = "NO"
                break
            else:
                stack.pop()

    if len(stack) != 0:
        result = "NO"

    print(result)




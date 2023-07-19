n = int(input())

result = [1, 2] * int((n/2)) + ([3] if n%2 else [])
print(*result)
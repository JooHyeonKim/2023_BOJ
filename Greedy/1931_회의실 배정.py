import sys
input = sys.stdin.readline

n = int(input())

meet = []

for _ in range(n):
    s, e = map(int,input().split())
    meet.append([s,e])


meet.sort(key = lambda x: (x[1],x[0]))

result = []
result.append(meet[0])
cnt=1

for i in range(1,n):
    previous = result[-1]
    if previous[1] <= meet[i][0]:
        result.append(meet[i])
        cnt += 1

print(cnt)
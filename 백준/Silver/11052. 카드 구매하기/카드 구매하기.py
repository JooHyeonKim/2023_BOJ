n = int(input())
p = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for x in range(1, n+1):
    for i in range(x):
        dp[x] = max(dp[x], dp[i]+p[x-i])
        #print("x =", x, "i =",i, "dp[",x,"]=", dp[x])

print(dp[n])
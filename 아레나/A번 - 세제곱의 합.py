n = int(input())

sum = 0
res = 0
for i in range(1,n+1):
    sum+=i
    res += i*i*i

print(sum)
print(sum*sum)
print(res)
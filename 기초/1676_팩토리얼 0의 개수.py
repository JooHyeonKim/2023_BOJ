import math

n = int(input())

fact = math.factorial(n)
flist = [int(x) for x in str(fact)]

cnt = 0

for i in range(len(flist)-1, -1, -1):
    if flist[i] == 0:
        cnt += 1
    else:
        print(cnt)
        break

n = int(input())
data = [0] * 1000001

for i in list(map(int, input().split())) :

    data[i] += 1

result = 0

for i in list(map(int, input().split())) :

  if data[i] >= 1 :
    data[i] -= 1
  else :
    result += 1

print(result)
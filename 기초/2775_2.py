T = int(input())

for i in range(T):
    height = int(input())  # 층
    weight = int(input())  # 호
    lst = [j for j in range(1, weight + 1)]  # 0층

    for k in range(1, height + 1):  # 1층~height층
        for l in range(1, weight):
            lst[l] += lst[l - 1]
    print(lst[weight - 1])
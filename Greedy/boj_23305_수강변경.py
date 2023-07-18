n = int(input())  # 학생 수

have = list(map(int, input().split()))  # 갖고 있는거
want = list(map(int, input().split()))  # 듣고 싶은거

result = n   # 최종 결과 : 원하는 수업을 못듣는 학생 수

for i in range(n):  # want 배열 탐색
    for j in range(n):  # have 배열 탐색

        print(have)
        print(want)
        print()

        if want[i] == have[j] and i != j:  # 내가 듣고 싶은걸 갖고 있는 사람이 있다면
            have[i], have[j] = have[j], have[i]  # 교환

            # 교환한 두 명이 원하는 수업을 얻었는지 확인

            if have[j] == want[j]:
                result -= 1
                have[j] = -1

            if have[i] == want[i]:
                result -= 1
                have[i] = -1  # 이후에 교환되지 않도록 -1로 설정
                break


#print(have)
#print(want)
print(result)




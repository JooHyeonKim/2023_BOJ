import sys

input = sys.stdin.readline

n = int(input())

word = []

for _ in range(n):
    word.append(input())

word2 = set(word)
word = list(word2)
word.sort()
word.sort(key = len)


for w in word:
    print(w, end='')
import sys

input = sys.stdin.readline

word = input()
alpha = list(range(97,123))

for a in alpha:
    print(word.find(chr(a)), end = ' ')

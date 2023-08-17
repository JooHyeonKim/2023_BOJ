

while(True):
    stack = []
    res = "yes"
    words = input()
    if words == "." and len(words) == 1:
        break

    for w in words:
        if w == '(':
            stack.append('(')

        elif w == ')':
            if len(stack) > 0 and stack[-1] == '(':
                stack.pop()
            else:
                res="no"
                break


        elif w == '[':
            stack.append('[')

        elif w == ']':
            if len(stack) > 0 and stack[-1] == '[':
                stack.pop()
            else:
                res = "no"
                break

    if len(stack) == 0:
        print(res)
    else:
        print("no")

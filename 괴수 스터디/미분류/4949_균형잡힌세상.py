
import sys
sys.stdin = open('test.txt')

while True:
    result = 'yes'
    text = input()
    ls = []

    if text == '.':
        break

    for i in text:
        if i == '.':
            break

        if i == '[' or i == '(':
            ls.append(i)
        elif i == ']':
            if ls:
                if ls[-1] != '[':
                    result = 'no'
                    break
                else:
                    ls.pop()
            else:
                result = 'no'
                break
        elif i == ')':
            if ls:
                if ls[-1] != '(':
                    result = 'no'
                    break
                else:
                    ls.pop()
            else:
                result = 'no'
                break
    else:
        if ls:
            result = 'no'

    print(result)



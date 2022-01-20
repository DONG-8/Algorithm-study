N = int(input())



for n in range(N):

    string = input()

    length = len(string)
    ls = []
    for i in range(length):

        if string[i] == ')':
            if ls:
                ls.pop()
            else:
                result = 'NO'
                break
        else:
            ls.append(string[i])
    else:
        if ls:
            result = 'NO'
        else:
            result = 'YES'

    print(result)

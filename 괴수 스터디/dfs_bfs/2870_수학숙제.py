N = int(input())
number = "0123456789"
test = []
for i in range(N):
    word = input()
    check = ""
    for k in range(len(word)):
        if word[k] in number:
            check += word[k]
        else:
            if check != "":
                test.append(check)
                check = ""
    if check:
        test.append(check)

test = list(map(int, test))
test.sort()
for w in test:
    print(w)

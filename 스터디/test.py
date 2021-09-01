import sys
sys.stdin = open('input.txt')

for t in range(10):
    T = int(input())
    wordboard = [list(input()) for _ in range(100)]
    max_len = ''
    # 리스트 안에 리스트가 있는 형태

    for k in range(100):
        for i in range(100):
            word = ''
            for j in range(i+1,100): # 100 - i
                word += wordboard[k][j]
                if word == word[::-1] and len(word) > len(max_len):
                    max_len = word
    # print(len(max_len))

    for i in range(100):
        for j in range(100):
            if i < j:
                wordboard[i][j], wordboard[j][i] = wordboard[j][i], wordboard[i][j]

    # print(len(max_len))
    # print()
    for k in range(100):
        for i in range(100):
            word = ''
            for j in range(i+1,100):
                word += wordboard[k][j]
                if word == word[::-1] and len(word) > len(max_len):
                    max_len = word

    print(len(max_len))


    # print(len(max_len))
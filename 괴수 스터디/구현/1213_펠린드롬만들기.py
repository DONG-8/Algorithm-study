word = list(input())
arr = [0] * 50
english =list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
for w in word:
    arr[english.index(w)] += 1
check_odd = 0
answer = ""
center_word = ""
for i in range(len(english)):
    if arr[i] and arr[i] % 2 == 0:
        answer +=  english[i] * (arr[i]//2)
    elif arr[i] and arr[i] % 2 != 0:
        answer += english[i] * (arr[i] // 2)
        center_word = english[i]
        check_odd += 1
    if check_odd >=2:
        print("I'm Sorry Hansoo")
        exit()

answer = answer + center_word + answer[::-1]
print(answer)

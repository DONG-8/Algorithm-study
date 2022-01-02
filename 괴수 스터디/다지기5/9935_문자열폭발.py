import sys
# 1. 브루트포스
# 2. 스택, 큐


# 입력받기
word = sys.stdin.readline().rstrip()
boom = sys.stdin.readline().rstrip()

# 폭발 길이만큼 슬라이싱 할 예정
boomlength = len(boom)

stack = []
# and len(stack) >= boomlength
for w in word:
    stack.append(w)
    if stack[-1] == boom[-1]:
        if boom == "".join(stack[-boomlength:]):
            for _ in range(boomlength):
                stack.pop()

if stack:
    print("".join(stack))
else:
    print("FRULA")


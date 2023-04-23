A,B,C = map(int, input().split())

# A의 거듭 제곱을 구하시오. 대신 너무 크니까 C로 나눈 나머지를 구하시오

def divide(A,B):
    if B == 1:
        return A % C
    elif B == 2:
        return A*A % C
    else:
        half = divide(A,B//2)   # 2의 6승이라면, 2의 3승을 구해서 답을 구함
        # 그럼 2의 3승은 2를 2번 곱하고 2를 한번 더 곱하는거지
        if B % 2 == 0:
            return half * half % C
        else:
            return half * half * A % C

result = divide(A,B)
print(result)
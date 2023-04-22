n,b = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def mul(n,A,B):
    new_arr = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                new_arr[i][j] += A[i][k] * B[k][j]
            new_arr[i][j] %= 1000
    
    return new_arr

def cal(n,b,A):
    if b == 1:
        return A
    elif b == 2:
        return mul(n,A,A)
    else:
        # 숫자가 2보다 클 경우
        # 예를 들어서 5이라면 A^2 * A^2 * A
        half = cal(n,b//2,A) # B를 절반의 제곱 값을 찾으러 간다
        if b % 2 == 0:
            return mul(n,half,half)
        else:
            return mul(n,mul(n,half,half),A)

result = cal(n,b,arr)
for i in range(n):
    for j in range(n):
        print(result[i][j]%1000,end=" ")
    print()
'''
LCS 2번째 버전
LCS를 출력하는 단계가 추가 되었다.
DP를 비교할 때 길이가 더 긴걸 비교해서 넣게 하되,
안에 채우는 내용은 문자열로 채워서 마지막 내용에서 바로 찾을 수 있게 한다.

'''

A = input()
B = input()
A_list = [""]
B_list = [""]
for k in A:
    A_list.append(k)
for k in B:
    B_list.append(k)

# print(A_list,B_list)

# 0번 가로세로 인덱스는 비워줘서 채울 수 있게 만들어준다.
dp = [["" for _ in range(len(B)+1)] for i in range(len(A)+1)]
# print(dp)

for i in range(1,len(A)+1):
    for j in range(1,len(B)+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + A[i-1]
        else:
            lf = len(dp[i][j-1])
            up = len(dp[i-1][j])
            if lf > up:
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]

print(len(dp[-1][-1]))
print(dp[-1][-1])


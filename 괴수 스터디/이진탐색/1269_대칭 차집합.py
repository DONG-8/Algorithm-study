N,M = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
print(len(set(A^B)))
# 교집합 구하기

# 지민이의 말 진실 or 과장
# 어떤사람이 진실을 알고있으면 무조건 진실을 말해야한다.

# N : 사람의 수 , M : 파티의 수
N, M  = map(int,input().split())

# 둘째줄 
# 0번 인덱스 : 진실을 아는 사람의 수 그 갯수만큼 사람들의 번호가 주어짐
a = list(map(int, input().split()))

if len(a) == 1:
    print(M)

else:
    pass


check_True = [0 for _ in range(N+1)]

if len(a):
    for i in range(len(a)):
        check_True[i] = i



print(check_True)
# 각 파티정보 확인
for i in range(M):
    k = list(map(int,input().split()))
    
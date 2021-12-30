'''
N 명의 사람과 N개의 일이 있다.

-- 조건
각일을 담당하는 사람은 한명
사람은 일을 1개 담당

Dij를  i번 사람이 j번 일을 할 때 필요한 비용이라고 했을 때,
모든 일을 하는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

1 <= N <= 20
둘째줄 N개줄 D의 내용이 주어짐
비용은 10000 보다 작거나 같은 자연수.
'''
# 입력

# 비트를 이용한 방문여부 처리
# 순회는 해야하기때문에 두고

# 각 선택별 작은 값을 비교

# 비트 없이 한다면?
# 1311 할 일 정하기 1

N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]
# visited = [False for i in range(N)]
dp = [[9999999 for i in range(1 << N)] for j in range(30)]


def recur(cur, visit):

    # if cur == N:
    if visit == (1 << N) - 1: # 모든노드를 방문했다면 
        return 0

    if dp[cur][visit] != 9999999:  # 메모이제이션 해놓은 값이 있다면?
        return dp[cur][visit]

    for i in range(N):  # 처음 저장하는 경우라면 모든 노드를 순회
        bit = 1 << i
        if visit & bit:  # 이미 방문한 노드라면 skip
            continue
        dp[cur][visit] = min(dp[cur][visit], recur(cur + 1, visit | bit) + arr[cur][i])

    return dp[cur][visit]


print(recur(0, 0))
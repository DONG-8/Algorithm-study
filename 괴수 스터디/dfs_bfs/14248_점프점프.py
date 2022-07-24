'''
점프점프

개구리다 개굴개굴
돌다리 숫자 --> 숫자만큼 왼쪽 or 오른쪽 점프가능

- 방향 벡터 왼쪽 오른쪽
- 돌다리 밖 x

돌다리에서 자기가 방문 가능한 돌들의 개수를 알고 싶어한다.

방문가능하다 === 현재 위치에서 다른 돌을 적절히 밟아 해당하는 위치로 이동이 가능하다는 뜻이다.

현재 위치가 주어졌을때 영우가 방문 가능한 돌드르이 개수를 출력하시오

'''

from collections import deque


def bfs():
    q = deque()
    q.append(start-1)
    result = 1
    visit[start - 1] = 1
    while q:
        my_x = q.popleft()
        jump = arr[my_x]

        r = jump + my_x
        l = my_x - jump
        goto = [r, l]
        for i in range(2):
            if 0 <= goto[i] < n and visit[goto[i]] == 0:
                visit[goto[i]] = 1
                result += 1
                q.append(goto[i])

    return result

def find_one():
    result = 0
    for i in range(n):
        if visit[i] == 1:
            result += 1

    return result


n = int(input())
arr = list(map(int, input().split()))

start = int(input())
visit = [0] * n
result = 1
## 방문한곳은 다시 들릴 필요가 없음
print(bfs())





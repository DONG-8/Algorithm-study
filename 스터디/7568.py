# 7568.py

# 덩치

'''

(x,y), (p,q)
x > p 그리고 y > q 이라면 우리는 A의 덩치가 B의 덩치보다 "더 크다"고 말한다.

예를 들어 두 사람 C와 D의 덩치가 각각 (45, 181), (55, 173)이라면
몸무게는 D가 C보다 더 무겁고, 키는 C가 더 크므로,
"덩치"로만 볼 때 C와 D는 누구도 상대방보다 더 크다고 말할 수 없다.

'''


# 입력
N = int(input())
ls = []
i = 0
while i < N:
    ls.append(list(map(int, input().split())))
    i += 1

print(ls)
# 자신보다 더 큰 덩치인 사람을 찾는다.
result = []
for bibigo in ls:
    count = 0
    for idx_num in range(N):
        if bibigo[0] < ls[idx_num][0] and bibigo[1] < ls[idx_num][1]:
            count += 1
    result.append(count+1)

print(*result)

        
   








'''
평범한 배낭에 관한 문제이다.
최대한 가치있게 배낭을 싸려고 한다.

n개의 물건, 무게 w, 가치 v 를 가지는데 v만큼 즐길 수 있다.
k만큼의 무게만 넣을 수 잇는 배낭만 들고 다닌다.

구하고자 하는것 ==> 준서가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의
                    가지츼 최댓값을 알려주자
'''

# 입력
N, K = map(int, input().split())

wv = [[0]]
ls = [[0]*(K+1) for _ in range(N+1)]

for i in range(N):
    wv.append(list(map(int,input().split())))

# 자체 무게가 크냐, 무게 조합이 크냐
for i in range(1,N+1):
    for j in range(1,K+1):
        w = wv[i][0]
        v = wv[i][1]

        if j < w:
            ls[i][j] = ls[i-1][j]
        else:
            ls[i][j] = max(v+ls[i-1][j-w],ls[i-1][j])

print(ls[N][K])
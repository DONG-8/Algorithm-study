N = int(input()) # 전구 갯수

switch = [0] + list(map(int, input().split()))
# 스위치 입력받기

PN = int(input())

for _ in range(PN):
    se, idx_num = map(int, input().split())
    if se == 1:
        for i in range(1,101):
            if 0 < idx_num*i < N+1:
                switch[idx_num*i] = (switch[idx_num*i]+1)%2
    else:
        # 여자일 때
        start = idx_num
        end = idx_num + 1
        for j in range(1, N+1):
            # 두개 다 범위 내에 있고, switch[idx_num-i] == switch[idx_num+i]: 양쪽 대칭이라면
            if 0 < idx_num-j < N+1 and 0 < idx_num+j < N+1 and switch[idx_num-j] == switch[idx_num+j]:
                start = idx_num - j
                end = idx_num + j + 1
            else:
                break
        # 끝나고 나서

        for wm in range(start,end):
            switch[wm] = (switch[wm]+1) % 2

switch = switch[1:N+1]
for i in range(0, N, 20):
    print(*switch[i:i+20])
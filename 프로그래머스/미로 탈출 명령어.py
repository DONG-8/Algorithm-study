'''
경로 중복 가능 -> 결과 도착했을때 짝수번 남은게 아니면 다시 못돌아옴
문자열 사전순으로 빠른 경로, 이동했을때 조건이 맞고 갈 수 있는 거리합이 k 보다 작은경우
direction을 사전순으로 나열하여 먼저 되는것이 가장 최적
'''
from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = ''
    arr = [[0]*(m+1) for _ in range(n+1)]
    q = deque()
    q.append((x,y,"",0))
    direction = [(1,0,"d"),(0,-1,"l"),(0,1,"r"),(-1,0,"u"),]    # 순서대로 배치
    # 다 탐색할 필요가 있을까?
    while q:
        sx, sy,word, cnt = q.popleft()
        if sx == r and sy == c and cnt == k:
            return word
        
        for i in range(4):
            nx,ny,nw = sx + direction[i][0], sy + direction[i][1],word + direction[i][2]
            if nx <= 0 or nx > n or ny <= 0 or ny > m: continue
            if abs(nx - r) + abs(ny - c) + cnt + 1 > k:continue
            q.append((nx,ny,nw,cnt + 1))
            break
    return "impossible"

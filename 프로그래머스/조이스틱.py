def solution(name):
    answer = 0
    up_down_count = 0
    left_right_count = 0
    visit = [0] * len(name)
    # print(ord("A"),ord("Z")) // 65 90
    # 이 값을 기준으로 알파벳의 값을 구함
    for sp in range(len(name)):
        if name[sp] == "A":
            visit[sp] = 1
        up = ord(name[sp]) - 65
        down = 91 - ord(name[sp])
        up_down_count += min(up,down)
    
    # 1이 있으면 한번 더 탐색하기
    # 각 위치에서 좌우로서의 최선의 거리 탐색
    # 같다면 오른쪽으로 쭉 이동할 수 있도록 지정
    # 결국 간 방향에 대해서 최소한의 이동 횟수를 찾아야함
    num = []
    def recur(idx,move,name,num,visit):
        if sum(visit) == len(name):
            c = move
            num.append(move)
            return
        
        lp,rp = 0,0
        
        l,r = idx,idx
        while visit[l] == 1:
            l = (l-1)%len(name)
            lp += 1
        
        while visit[r] == 1:
            r = (r+1)%len(name)
            rp += 1
        visit[l] = 1
        recur(l,move + lp,name,num,visit)
        visit[l] = 0
        visit[r] = 1
        recur(r,move + rp,name,num,visit)
        visit[r] = 0
            
        
    recur(0,0,name,num,visit)

    return up_down_count + min(num)
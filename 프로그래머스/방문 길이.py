def solution(dirs):
    answer = 0
    # 총11 개의좌표이기 때문에 11개를 만들어준다
    arr = [[0]*11 for _ in range(11)]
    visit = []
    x,y = 5,5
    
    # U,D,R,L
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    # 좌표 이동만 해주면서 방문 여부만 체크하고, 경계를 넘어가는 명령어라면 원래대로 둔다
    for cm in dirs:
        fx,fy = x,y
        
            
        if cm == "U":
            nx = fx + dx[0]
            ny = fy + dy[0]
        elif cm == "L":
            nx = fx + dx[3]
            ny = fy + dy[3]
        elif cm == "R":
            nx = fx + dx[2]
            ny = fy + dy[2]
        else:
            nx = fx + dx[1]
            ny = fy + dy[1]
        
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            # 다닌 거리를 추가 해 줌
            visit.append((fx,fy,nx,ny))
            visit.append((nx,ny,fx,fy))
            x,y = nx,ny        
        
    return len(set(visit))//2
# 결과 boolen
# 가능한지만 알아내면됨
# 회전 하고 이동할 수 있는

def solution(key, lock):
    answer = True
    N,M = len(lock),len(key)
    rotate_key = []
    
    
    for i in range(M):
        for j in range(M):
            if key[i][j] == 1:
                rotate_key.append([i,j])
    lock_point = []
    for i in range(N):
        for j in range(N):
            if lock[i][j] == 0:
                lock_point.append((i+M-1,j+M-1))    
    lock_point = set(lock_point)
    def rotate_clock(pointer):
        key_pointer = []
        for i,j in pointer:
            key_pointer.append([j,M-i-1])
        return key_pointer
    
    # 4번의 검증 과정이 필요함.
    for _ in range(4):
        for i in range(N+M):    # 총 1600
            for j in range(N+M):
                check = set()
                for x,y in rotate_key:
                    nx = x + i
                    ny = y + j
                    if M-1 <= nx < N+M-1 and M-1 <= ny < N+M-1:
                        check.add((nx,ny))
                if check == lock_point:
                    return True
        
        rotate_key = rotate_clock(rotate_key)
        rotate_key.sort()
    return False
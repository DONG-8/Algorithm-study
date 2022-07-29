def solution(numbers, hand):
    # 손의 이동을 기록하기 위한 str
    answer =''
    # 키패드 위치 정의
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    
    # 시작지점 확인
    left_hand = dic['*']
    right_hand = dic['#']
    
    for i in range(len(numbers)):
        
        if numbers[i] in [1,4,7]:
            answer += "L"
            left_hand = dic[numbers[i]]
        elif numbers[i] in [3,6,9]:
            answer += "R"
            right_hand = dic[numbers[i]]
        elif numbers[i] in [2,5,8,0]:
            # 거리계산
            x,y = dic[numbers[i]]
            lx,ly = left_hand
            rx,ry = right_hand
            if abs(x-rx) + abs(y-ry) == abs(x-lx) + abs(y-ly):
                if hand == 'right':
                    answer += "R"
                    right_hand = dic[numbers[i]]
                else:       
                    answer += 'L'
                    left_hand = dic[numbers[i]]
            elif abs(x-rx) +abs(y-ry) > abs(x-lx) + abs(y-ly):
                answer += "L"
                left_hand = dic[numbers[i]]
            else:
                answer += "R"
                right_hand = dic[numbers[i]]
    
    return answer
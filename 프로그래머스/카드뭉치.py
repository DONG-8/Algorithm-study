def solution(cards1, cards2, goal):
    answer = ''
    # 교차 que를 이용한 목표 배열 만들기    
    flag = False
    # 길이 결정
    i = 0
    while i < len(goal):
        word = goal[i]
        if cards1 and word == cards1[0]:
            cards1.pop(0)
            i += 1
        elif cards2 and word == cards2[0]:
            cards2.pop(0)
            i += 1
        else:
            return "No"
    return "Yes"
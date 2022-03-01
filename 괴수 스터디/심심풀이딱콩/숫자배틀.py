def mitjang(arr):

    mitjangppagi = [1,2,3,4,5,6]
    for i in arr:
        if i not in arr:
            return(True)



def num_fight(p1,p2):
    # 문제의 조건들에 맞추어 코딩하세요
    # 게임 촉 횟수 6회
    gamecount = 6
    # 개인이 낸 숫자가 냈던 값인지 확인
    player1_numberCheck = [0]*7
    player2_numberCheck = [0]*7
    result = ''
    # 만약 리스트중에 값이 다른것이 있을경우 동작으만 밑장빼기 리턴
    if mitjang(p1) or mitjang(p2):
        return('동작그만 밑장빼기냐?')
    
    # 이제 중복체크만합시다
    p1win = 0
    p2win = 0
    for i in range(gamecount):
        # 각자 처음 낸 번호 확인
        a,b = p1[i],p2[i]
        # 중복체크
        if player1_numberCheck[a] == 1 or player2_numberCheck[b] == 1:
            return('동작그만 밑장빼기냐?')
        
        # 사용한 숫자라고 체크해줌
        player1_numberCheck[a] = 1
        player2_numberCheck[b] = 1
        if a > b:
            p1win += 1
        elif a < b:
            p2win += 1
        else:
            pass
            
    if p1win > p2win:
        return('player1 승리')
    elif p1win < p2win:
        return('player2 승리')
    else:
        return('서로 비겼습니다')

            

        

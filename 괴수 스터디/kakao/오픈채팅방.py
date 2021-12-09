def solution(record):
    answer = []
    
    return answer


# 채팅방에 들어올 때 메시지출력
# "[닉네임]님이 들어왔습니다."

# 나가면 나갔습니다.


# 닉네임 변경 2가지분기점

# 1. 나간 후 새로운 닉네임으로 다시 들어옴
# 2. 채팅방에서 닉네임을 변경한다.

# 근데 나가서 변경하고 와도 기존에 출력되었던 내용이 다시 바뀜

# 그럼 그 아이디가 있으면
# 그냥 같이 한번에 탐색해서 바꿔주고

stat = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result = []
for i in stat:

    user_informs = i.split()
    result.append(user_informs)

# 핵심키는 userid
# 들어왔다 나갔다에 대한 입력 따로, id는 변경되서 마지막에 넣도록

# user닉네임을 넣어줄 딕셔너리 생성 , 계속 갱신
user_nickname = dict()
for i in result:
    if len(i) == 3:
        if i[0] == 'Enter':
            user_nickname[i[1]] = i[2]
        elif i[0] == "Change":
            user_nickname[i[1]] = i[2]
        else:
            user_nickname.pop(i[1])

# 딕셔너리에 모든 정보가 담겼다. 이제 이 정보를 통해 user id의 value를 가져와서 데이터에 삽입
informations = []

# print(user_nickname.get('uid4567'))

for i in result:

    if i[0] == 'Enter':
        a = user_nickname.get(i[1])
        b = a + "님이 들어왔습니다."
        c = '{}'.format(b)
        # print(c)
        informations.append(c)
        # print(informations)
    
    elif i[0] == 'Leave':
        a = user_nickname.get(i[1])
        b = a + "님이 나갔습니다."
        c = '{}'.format(b)
        # '\"{}\"'.format(b)
        informations.append(c)
    else:
        pass




        
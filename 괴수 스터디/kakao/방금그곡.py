def solution(m, musicinfos):
    answer = ''
    return answer


# 네오가 찾으려는 음악 제목을 구하라

# 멜로디와 악보에 사용되는 음 리스트

melody = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

m = "ABCDEFGHI"
muzi_want_music = []
for i in range(len(m)):
    if '#' == m[i]:
        a = muzi_want_music.pop().lower()
        muzi_want_music.append(a)
        continue
    muzi_want_music.append(m[i])

m = ''.join(muzi_want_music)
melody_length = len(muzi_want_music)
musicinfos = ["03:00,03:30,FOO,ABCDEFGHI", "04:00,04:31,BAR,ABCDEFGHI"]

# 하나의 문자열에서
# 끝시간 - 시작시간 차이 문자열 길이

# 음악의 반복성 --> 1.HH : MM 두개 차이로 시간확인 1439길이기때문에 언제까지 반복될지모른다
result = []
for k in range(len(musicinfos)):
    # 음악정보 각각 분해
    # 0번 인덱스 시작시간
    # 1번 인덱스 종료시간
    # 2번 인덱스 음악제목
    # 3번 악보
    info = musicinfos[k].split(',')

    # 시간 구하기
    start = info[0].split(":")
    end = info[1].split(":")
    hour = int(end[0]) - int(start[0])
    minit = int(end[1]) - int(start[1])
    if minit < 0:
        hour -= 1
        minit = 60 + minit
    # 음악 제목을 title 라는 변수에 할당
    title = info[2]

    # 현 음악의 playtime을 계산한다.
    playtime = hour*60 + minit
    # print(playtime)

    find_music = []
    for i in range(len(info[3])):
        if '#' == info[3][i]:
            a = find_music.pop().lower()
            find_music.append(a)
            continue
        find_music.append(info[3][i])
    print(find_music)
    count = 0
    check = 0
    i = 0

    list_of_searchmusic = []
    while count < playtime:
        i = i%len(find_music)
        print(i)
        list_of_searchmusic.append(find_music[i])
        count +=1
        i += 1
    
    # list_of_searchmusic 에는 찾고자 하는 노래의 플레이 시간만큼의 멜로디가 들어 가 있다

    # 일치하는것이 있다면 담는다.
    
    # 일치하는것을 찾아보자

    # a = ['a','b','c'] in ['a','b','c','d']
    # print(a)
    # k = 'abc' in 'abcde'
    # print(k)
    
    list_of_searchmusic = ''.join(list_of_searchmusic)
    # print(list_of_searchmusic, m)

    # print(list_of_searchmusic, m)
    # print(a)
    if m in list_of_searchmusic:
        result.append([playtime,k,title])

result.sort(key = lambda x : (-x[0],x[1]))
print(result)

# # print(result)
# if len(result) >= 2:
#     result.sort(lambda x : (-x[0],x[1]))
#     print(result[0][2])

# elif len(result) == 1:
#     print(result[0][2])

# else:
#     print('NONE')


# result.sort(lambda x : (-x[0],x[1]))


# 20, 21 22 23 27 28 29 30



    
    # 조건이 일치하는 음악이 여러개 일때는 처음나온 음악




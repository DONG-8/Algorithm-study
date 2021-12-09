
'''
1초 후 이동할 수 있는 장소
+1 -1 *2
'''

# # 깊이로 가버리면 문제가 풀리지 않는다.
# def recur(location_of_subin, time):
#     # 가지치기를 위한 최소값 보다 큰 시간이나오면바로 종료
#     global min_time,K

#     # 종료조건
#     if location_of_subin == K:
#         if min_time > time:
#             min_time = time
#         return

#     # 가지치기
#     if time >= min_time:
#         return

#     if K - location_of_subin >= 0:
#         for i in range(2)

N, K  = map(int,input().split())

# 최단거리 문제, bfs 사용 --> while문 사용
que = [N]
count = 0
visit = [0]*100002

if N == K:
    print(0)
    exit()

else:
    while que:

        count += 1
        # que 의 길이 만큼 반복, 이것이 한번의 각자 깊이로 들어간 좌표들의 갯수임
        for j in range(len(que)):
            # 가장 왼쪽에 있는 값 하나 빼오기!
            a = que.pop(0)

            for i in (a -1, a +1, a*2):
                if 0 <= i <= 100000 and visit[i] == 0:
                    visit[i] = 1
                    if i == K:
                        print(count)
                        exit()
                    que.append(i)
        


        # print(count)
        # for j in range(len(que)):
        #     N = que.pop(0)
        #     print(j,'지금 que의 길이')
        #     # print(N,'현재 수빈이의 위치')
        #     for i in range(3):
        #         if 0<= N < 100001 and visit[N] == 0:
        #             visit[N] = 1

        #             if i== 2:
        #                 a = N * 2
        #             else:
        #                 a = N + list_of_path[i]
                    
        #             print(a,'이동하게 될 위치')
        #             if a == K:
        #                 print(count)
        #                 exit()
        #             else:
        #                 que.append(a)
        #                 print('내부의 각 좌표별로 이동했습니다.')


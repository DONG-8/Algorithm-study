'''
Q 10만
k -> 한 쿼리에서의 정보의 수 10만
# 1일때와 아닐때~
# 그리고 내부의 값을 최대값만 최대만 빠르게 뽑아낼 수 있도록 heap 자료구조
'''
import heapq
Q = int(input())


dic = {}
answer = 0
answer_arr = []
for _ in range(Q):
    info = list(input().split())    # 정보 분열해서 담기
    if info[0] == "1":
        # 정보 업데이트
        a = dic.get(info[1],[])
        a += list(map(int, info[3:]))
        dic[info[1]] = a
    else:
        # 필요한 갯수 만큼의 값을 빼내고, 정보 리스트 초기화
        # 빼낸 값은 결과에 담아준다.
        a = dic.get(info[1],[])
        if a == [] or len(a) <= int(info[2]):
            answer_arr += a
            dic[info[1]] = []
        else:
            # for i in range(len(a)):
            #     a[i] = -1 * a[i]
            # heapq.heapify(a)
            # for j in range(int(info[2])):
            #     answer_arr.append(-1 * heapq.heappop(a))
            # for k in range(len(a)):
            #     a[k] = -1*a[k]
            a.sort()
            for i in range(int(info[2])):
                answer_arr.append(a.pop())
            dic[info[1]] = a


# print(answer_arr)
print(sum(answer_arr))

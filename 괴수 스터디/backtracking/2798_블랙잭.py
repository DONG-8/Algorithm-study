'''

블랙잭 재귀풀이

3개 선택 -> 568 658 같은거
중복 없는 리스트 만들기

재귀함수 안에서 처리
or 리스트 완성 후 밖에서 내용 처리

더해지는 값 21 에 가까울수록 선택

'''
import sys
sys.stdin = open('test.txt')

n, m = map(int,input().split())
num_list = list(map(int,input().split()))

# 선택 했냐 안했냐의 문제

# 중복되지않는 숫자들의 집합을 만든다

arr = [0]*3
result = 0
def recur(cur,start):
    global result

    if cur == 3:
        if sum(arr) <= m and m-result > m-sum(arr):
            result = sum(arr)
        return

    for i in range(start, n):
        arr[cur] = num_list[i]
        recur(cur+1, i+1)


recur(0,0)
print(result)


# result = 0
# def recur(cur,cnt,tot):
#     global result
#
#     if cnt == 3:
#         if abs(m - result) > abs(m - tot):
#             result = tot
#         return
#
#     if cur == n:
#         return
#
#     tot += num_list[cur]
#     recur(cur+1, cnt+1, tot)
#     tot -= num_list[cur]
#     recur(cur+1, cnt, tot)
#
# recur(0,0,0)
# print(result)


#
# def recur(cur,start,tot):
#     global result
#
#     if cur == 3:
#         if m-result > m-tot:
#             result = tot
#             return
#
#     for i in range(start,m):
# #         if visited[i]:
# #             continue
#
#         visited[i] = 1
#         tot += num_list[i]
#         recur(cur+1,i,tot)

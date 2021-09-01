# 로프
'''
문제 조건
N(1 ≤ N ≤ 100,000)개의 로프가 있다. 
이 로프를 이용하여 이런 저런 물체를 들어올릴 수 있다. 
각각의 로프는 그 굵기나 길이가 다르기 때문에 들 수 있는 물체의 중량이 서로 다를 수도 있다.

하지만 여러 개의 로프를 병렬로 연결하면 각각의 로프에 걸리는 중량을 나눌 수 있다. 
k개의 로프를 사용하여 중량이 w인 물체를 들어올릴 때, 각각의 로프에는 모두 고르게 w/k 만큼의 중량이 걸리게 된다.

각 로프들에 대한 정보가 주어졌을 때, 
이 로프들을 이용하여 들어올릴 수 있는 물체의 최대 중량을 구해내는 프로그램을 작성하시오.
모든 로프를 사용해야 할 필요는 없으며, 임의로 몇 개의 로프를 골라서 사용해도 된다.

-------------입력

첫째 줄에 정수 N이 주어진다. 
다음 N개의 줄에는 각 로프가 버틸 수 있는 최대 중량이 주어진다. 
이 값은 10,000을 넘지 않는 자연수이다.
'''
# 최소값 그다음 갯수 많을수록 좋음 결국 최소값을 구하고 길이만큼
n = int(input())

loap = [int(input()) for _ in range(n)]

loap.sort()
k = len(loap)
i = 0
ls = []
hot = min(loap)*k
while k:
    if loap[i]*k >= hot:
        hot = loap[i]*k
    i += 1
    k -= 1

print(hot)

# summ = []
# for i in range(len(loap)):
#     if int(a) <= loap[i]: # 평균에서 평균보다 큰수 찾기
#         sum.append(loap[i]) # 리스트 만들기
    
# p = min(sum)*len(sum) # 리스트내부 최소값에 길이곱

# 이평균에 영향을 주는 것은 무엇인가
# 끊기는 밧줄이 있으면 평균이 바뀐다.

#  # 정렬
# # 작은값들부터 정렬

# 이 식들에서 변하는것은 밧줄의 갯수 k
# 무게의 합 :: 최소 값부터 근접
    



        



'''
 5 10 10 10 10 
지금 해볼려고 하는거있는데
볼래?
'''















# sibisiba = [] # 이걸 안써야겠네
# for i in range(1<<len(loap)):
#     llllssss = []
#     for j in range(len(loap)):
#         if i & 1<<j:
#             llllssss.append(loap[j])
#     sibisiba.append(llllssss)
# print(sibisiba)

# largest = []
# for lili in range(1,len(sibisiba)):
#     largest.append(min(sibisiba[lili])*len(sibisiba[lili]))

# print(max(largest))


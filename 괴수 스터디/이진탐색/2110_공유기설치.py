'''

N 개가 수직선 위에 있다. 각각의 집 좌표는 x1~~~ xN
C 개의 공유기를 N개의 집에 적당히 설치해서, 
가장 인접한 두 공유기 사이의거리를 최대로 하는 프로그램을 작성하시오.

'''
N, C = map(int,input().split())

house = []
for i in range(N):
    house.append(int(input()))

house.sort()
print(house)
'''
트리플 소트

알고리즘 수업을 듣고 감명받은 윤이는 
자신만의 정렬 알고리즘을 만들기로 했다.
- 배열에서 연속한 위치에 있는 세 원소를 임의로 고른다.
- 세 원소의 순소를 뒤집는다.
예를들어 세 원소가 순서대로 a,b,c이면 뒤집은 뒤에는 c,b,a가 된다.
배열이 오름차순으로 정렬될 때까지 위과정을 반복한다.

하지만 윤이는 트리플 소트로 모든 배열을 정렬할 수 없다는 사실을 깨닫고 실망
1 ~ N 까지의 정수가 한 번씩 등장하는 배열이 주어졌을 때,
트리플 소트로 정렬할 수 있는지 판별하는 프로그램을 작성하시오

'''

N = int(input())

arr = list(map(int, input().split()))

check= True
for i in range(N):
    # 홀수일때
    if i%2 == 1:
        if arr[i]%2 == 1:
            check = False
    else:
        if arr[i]%2 == 0:
            check = False

if check:
    print('YES')
else:
    print('NO')


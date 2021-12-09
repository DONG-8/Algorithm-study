import sys


N = int(sys.stdin.readline())

# 오름차순으로 입력이 된다.
num_list = list(map(int,sys.stdin.readline().split()))

# 단순 이미 정렬된 리스트에서 모든값을 비교하는것은 비효율적

# 최소값, 최소값을 만드는 각 값을 갱신 할 필요가 있다.

min_num = 9999999999999999999999


# 인덱스 값으로 갱신
left = 0
right = N-1

left_number = 0
right_number = 0

while left < right:

    sum_of_num = num_list[left] + num_list[right]

    if abs(sum_of_num) <= min_num:
        min_num = abs(sum_of_num)
        left_number = num_list[left]
        right_number = num_list[right]
    
    if sum_of_num < 0:
        left += 1
    
    elif sum_of_num > 0:
        right -= 1

    else:
        break

print(left_number,right_number)
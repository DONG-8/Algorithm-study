def solution(numbers):
    answer = 0
    numbers.sort()
    return numbers[-2] * numbers[-1]
import heapq

# 배열의 길이가 100만이므로 1회 반복 혹은 내부 반복문의 시간복잡도가 1으로 끝나야함
def solution(numbers):
    answer = [-1]*len(numbers)
    # 정렬은 내 이전에 나온 값들이 작은 값 부터
    # 1 2 7 4 6 8 -> 6일때 heap에는 7,4 현재 내가 가진 값보다 작은 값에만 뒤에있는 큰 수 이기 때문에
    # 7은 해당사항 없음 -> 이전에 나와있던 heap의 작은 값부터 빼와야함
    # 바로 뒤에 큰 값이 나오면 빠지고 종료
    heap = []
    # 해당 열을 기준으로 이전의 값에 대한 연산을 반복하는 방식
    for i in range(len(numbers)):
        value = numbers[i]
        while heap and heap[0][0] < value:
            v, idx = heapq.heappop(heap)
            answer[idx] = value
        heapq.heappush(heap, [value,i])
    
    return answer
# sequence의 길이가 50만이기 때문에, 연속 부분수열을 구해야한다.
# 연속 부분수열에서 펄스를 곱해줘야한다.
# 2가지 수를 기억하고 가야한다. 1로 시작한 펄스 , -1로 시작한 펄스
# 이를 통해 연속 펄스 부분 수열의 합의 최댓값을 갱신한다.
# O(n)

# 결국 각 index 에서 가지는 부분 수열의 최대값을 갱신해나가면 되는거지
def solution(sequence):
    answer = 0
    plus_start = sequence[:]
    minus_start = sequence[:]
    dp_p = [0] * len(sequence)
    dp_m = [0] * len(sequence)
    
    for i in range(len(sequence)):
        if i % 2 == 0:
            minus_start[i] *= -1
        else:
            plus_start[i] *= -1
    dp_p[0],dp_m[0] = plus_start[0],minus_start[0]
    # 펄스의 2가지 경우에 대한 배열 2가지를 구했다.
    for i in range(1,len(plus_start)):
        dp_p[i] = max(dp_p[i-1] + plus_start[i],plus_start[i])
    
    for i in range(1,len(minus_start)):
        dp_m[i] = max(dp_m[i-1] + minus_start[i],minus_start[i])

    return max(max(dp_m),max(dp_p))

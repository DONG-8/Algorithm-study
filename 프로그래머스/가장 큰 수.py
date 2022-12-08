def solution(numbers):
    answer = ''

    if max(numbers) == 0:
        return "0"
    numbers.sort(key = lambda x : -int((str(x)*4)[:4]))
    numbers = list(map(str, numbers))
    answer = "".join(numbers)
    
    return answer

    # 어떤 수가 올 수 있을지 모름
    # 그럼 어떻게 해야할까
    
    # 순서 쌍은 그대로 묶여야함
    
    # 자릿수 차이 때문에 생기는 문제임
    # 자릿수를 동일하게 만들어주고 비교해서 앞으로 빼내준다.
    
    # 총 10 자리 숫자를 만들어줄거임, 2순위는 길이
    # 3, 3000 // 30 3000 --> 3부터 오는게 좋음 길이가 짧은것 부터 넣어준다.
    # 틀림
    
    # 2안
    # 818 81 817 비교
    # 818818 818181 817817
    # 길이가 동일하게 만들어줘야함
    # 4자리 수니까 1자리수 4배 해야 4자리로 만듬 곱 4 해주고,  4만큼 슬라이스
    
import math

def get_time(arr):
    # 홀수인경우
    print(arr,'배열')
    minute = 0
    if len(arr)%2 == 1:
        for i in range(len(arr),-1,-2):
            # 처음의 경우에만 처리해준다.
            if i == len(arr):
                out_h,out_m = 23, 59
            else:
                out_h,out_m = map(int, arr[i].split(':'))   # 코중복 오반뎅
            in_h, in_m = map(int, arr[i-1].split(':'))
            outmin = 60*out_h + out_m
            inmin = 60*in_h + in_m
            minute += outmin-inmin
    else:
        for i in range(len(arr)-1,-1,-2):
            out_h,out_m = map(int, arr[i].split(':'))
            in_h, in_m = map(int, arr[i-1].split(':'))
            outmin = 60*out_h + out_m
            inmin = 60*in_h + in_m
            minute += outmin-inmin
    return minute
    
def solution(fees, records):
    
    answer = []
    # fees 0 : 기본시간, 1 : 기본요금, 2 : 단위시간, 3 : 단위요금
    # 출차내역이 없다면 23:59로 취급
    
    # 차량 번호와 출입을 구분하기위한 dic
    car_info = {}
    cars = []
    for i in records:
        time, car_num, state = i.split()
        if car_num in car_info:
            car_info[car_num].append(time)
        else:
            car_info[car_num] = [time]
            cars.append(car_num)
    cars.sort()
    
    for i in cars:
        arr = car_info[i]
        park_min = get_time(arr)
        print(park_min)
        
        # 기본요금 이하
        if park_min <= fees[0]:
            answer.append(fees[1])
        # 아닐때
        else:
            money = fees[1] + math.ceil((park_min-fees[0])/fees[2])*fees[3]
            answer.append(money)
    
    # 차량 번호가 작은 자동차부터 청구요금 정수배열 출력
    return answer
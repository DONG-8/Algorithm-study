while True:
    try:
        n = int(input())
        # 결국 1 11 111 1111 111111 11111111 이 n으로 나누어 떨어지는지 찾아야함
        one = 1
        i = 1
        while True:
            if one % n == 0:
                print(i)
                break
            else:
                one += 10 ** i
                i += 1
    except:
        break 
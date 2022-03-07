
N  = int(input())

def sum_of_st(st):
    # str의 합 구하기!
    a = ''.join(st)
    a = a.replace(" ",'')
    return eval(a)

    

def recur(cur, st):
    # 하나의 수가 체크 될때 더하기 혹은, -  혹은 더하기
    arr = ['+','-',' ']

    if cur == a:
        if sum_of_st(st) == 0:
            b = ''.join(st)
            ls.append(b)
        return

    for x in arr:
        st.append(x)
        st.append(str(cur+1))
        recur(cur+1,st)
        st.pop()
        st.pop()



for i in range(N):
    # 빈 리스트를 삽입 해 줍니다.
    ls = []

    a = int(input())
    # 1~a 까지 수 오름차순으로 정렬
    num = 0
    recur(1,['1'])
    # 1 ~ 입력받은 숫자까지 입력을 받음)
    ls.sort()
    for i in ls:
        print(i)

    print()

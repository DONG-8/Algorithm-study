'''

입력

암호 자릿수 4자리
서로 다른 L 개의 알파벳,
 --> 최소 한 개의 모음(a,e,i,o,u) 와 최소 두개의 자음으로 구성

C 언어의 갯수
다음줄 암호에 들어갈 언어
자음 모음 구분


정렬된 문자열을 선호하는 조교들의 성향 --> 증가하는순으로 배열

# 순서 o  중복 x 조합

4자리 조합 템플릿 써서 바로 완성

'''

def recur(N, start):

    if N == L:
        yes = 0
        check = 0

        for k in range(len(use)):
            if use[k] in a:
                yes = 1
            if use[k] not in a:
                check += 1


        if yes == 1 and check >= 2 :
            result = ''.join(use)
            print(result)
        return

    for i in range(start,C):
        use.append(arr[i])
        recur(N+1,i+1)
        use.pop()


L, C = map(int, input().split())

arr = list(input().split())
arr.sort()
a = ['a','e','i','o','u']
# print(arr)
use = []
recur(0,0)


'''
4 6
a t c i s u


'''

# 평균은 넘겠지

'''
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
둘째 줄부터 각 테스트 케이스마다 학생의 수 N이 첫 수로 주어지고,
이어서 N명의 정무사 주어진다. 점수는 0보다 크거나 같고, 100보다
작거나 같은 정수이다.

---
출력

각 케이스마다 한 줄씩 평균을 넘는 
비율을 반올림 하여 소수점 셋째 자리까지 출력한다.

'''

n = int(input())
fi = []
for i in range(n):
    ls = list(map(int, input().split()))
    fi.append(ls)

sss = 0
for ss in fi:
    sum_num = sum(ss[1::])
    avg= sum_num/ss[0]
    count = 0
    for i in ss[1::]:
        if avg < i :
            count += 1
    final = (count/ss[0])*100
    print("{:.3f}%".format(final))
    

 



n = int(input())
total_arr = [input() for _ in range(2*n)]

# in_Car = total_arr

# a b c d e
# b a d c e
# a랑 b 가 다르다 추월
# a가 나올때 까지는 체크 x
# c d 다르네? 그럼 다시 c 나올때 까지 체크
# 

in_arr = total_arr[0:n]
out_arr = total_arr[n:2*n]

for i in range(len(in_arr)):
    print(in_arr[i],'나와떠염')
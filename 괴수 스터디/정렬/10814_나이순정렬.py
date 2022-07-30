N  = int(input())
arr = []
# 가입순서 arr에 추가 후 정렬
for i in range(N):
    old , name = input().split()
    arr.append((int(old),name,i))
arr.sort(key = lambda x : (x[0],x[2]))
for i in range(N):
    print(arr[i][0],arr[i][1])
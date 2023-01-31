n = int(input())
arr = list(map(int, input().split()))
dp = [0]

for i in range(len(arr)):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        l,r = 0, len(dp)
        while l <= r:
            mid = (l+r)//2
            if dp[mid] >= arr[i]:
                r = mid-1
            else:
                l = mid +1
        dp[l] = arr[i]

print(len(dp)-1)
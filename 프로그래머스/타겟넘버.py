def dfs(cur,arr,num,target,com):
    if cur == len(arr):
        if num == target:
            com.append(1)
        return
    num -= arr[cur]
    dfs(cur+1, arr, num,target,com)
    num += arr[cur]
    num += arr[cur]
    dfs(cur+1, arr, num,target,com)
    num -= arr[cur]

def solution(numbers, target):
    answer = []
    # 더하거나 빼기
    dfs(0,numbers,0,target,answer)
    return len(answer)
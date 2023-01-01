
def solution(numbers):
    answer = 0
    # 재귀
    visit = [0] * len(numbers)
    word = ""
    combi = []
    def recur(cur,word,numbers,n):
        
        if cur == n:
            a = word[:]
            combi.append(a)
            return
        
        for i in range(len(numbers)):
            if visit[i] == 0:
                visit[i] = 1
                word += numbers[i]
                recur(cur+1,word,numbers,n)
                word = word[:-1]
                visit[i] = 0
    
    
    
    for i in range(1,len(numbers)+1):
        recur(0,word,numbers,i)
    
    arr =set( list(map(int, combi)))
    for n in arr:
        if n == 1 or n == 0:
            continue

        cnt = 0
        for i in range(2, n):
            if i * i > n:
                break

            if n % i == 0:
                cnt += 1

        if cnt == 0:
            print(n)
            answer += 1
    return answer
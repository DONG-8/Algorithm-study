from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    visited=[False]*(len(words))
    q=deque([(begin,0)])
    n=len(begin)
    k=len(words)
    answer=float('inf')
    while q:
        w,cnt=q.popleft()
        if w==target:
            answer=min(answer,cnt)
        for j in range(k):
            count=0
            for i in range(n):
                if words[j][i]!=w[i]:
                    count+=1
            # 1개만 달라야함
            if count==1 and not visited[j]:
                visited[j]=True
                q.append((words[j],cnt+1))

    return answer
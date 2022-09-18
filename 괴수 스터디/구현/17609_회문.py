def palindrome(left,right):
    global string
    
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    
    return True
    

# 이진탐색 gogo
T = int(input())

for t in range(T):
    string = input()
    # 10만의 탐색
    
    # 회문을 결정하는 방법 index 가 0일때는, 그냥 뒤집어서 맞으면 끝내기
    if string == string[::-1]:
        print(0)
        continue
    else:
        # 이진탐색
        left,right= 0, len(string)-1
        while left < right:
            if string[left] == string[right]:
            # 양 끝점이 같을때,
                left += 1
                right -= 1
            else:
            # 양 끝점이 다를때 문자열 하나를 제외해야함
            # acbccba --> 동일하게 건너 오다가 c - b에서 다름
            # left 1 , right 5
            # left의 문자를 뛰어넘기, right의 문자를 뛰어넘기
                # 이때 뛰어넘은 문자에 대해서 다시 재판별이 필요함
                left_result = palindrome(left +1, right)
                right_result = palindrome(left, right-1)
                if left_result or right_result:
                    print(1)
                else:
                    print(2)
                break
            
            # 왼 오 하나씩 제외했을때 결과값 확인하고 break
        
        
                
                            
        
        
    
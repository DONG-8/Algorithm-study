## 조건분기

word = input()
underCount = 0
upperCount = 0


## java c++ 구분
# _ 와 소문자, _ 와 다음단어가 소문자, 맨앞글자 소문자,
# _ _ x , _A , _asdfasdf , asdfaef_, ____ 밑줄 여러개
flag = False

for i in range(len(word)):
    if i == 0:
        if word[i] =="_" or word[i].isupper():
            flag = True
    
    if word[i] == "_":
        underCount += 1
        if i + 1 == len(word):
            flag = True
        
        else:
            if word[i+1].isupper():
                flag = True
            elif word[i+1] == "_":
                flag = True
    else:
        if word[i].isupper():
            upperCount += 1
    
if upperCount > 0 and underCount > 0:
    print("Error!")
    exit()
elif flag == True:
    print("Error!")
    exit()
            
result = ""
i = 0

while i < (len(word)):
    if word[i] == "_":
        result += word[i+1].upper()
        i+= 2
    elif word[i].isupper():
        result += "_" + word[i].lower()
        i += 1
    else:
        result += word[i]
        i += 1
    
print(result)
import sys
sys.stdin = open('input.txt')

def recur(start, cur):
    if cur == 3:
        aa = combi[:]
        a = find_hap(aa)
        if a == True:
            check.append(aa)
        return
    for i in range(start,9):
        combi.append(i)
        recur(i+1,cur + 1)
        combi.pop()


def find_hap(array):
    hap = [[],[],[]]
    a,b,c = array
    for i in range(3):
        hap[i].append(arr[a][i])
        hap[i].append(arr[b][i])
        hap[i].append(arr[c][i])

    for j in range(3):
        if len(set(hap[j])) == 1 or len(set(hap[j])) == 3:
            continue
        else:
            return False
    else:
        return True


dic = { "CIRCLE" : 0 , "TRIANGLE" : 1, 'SQUARE' : 2 , 'YELLOW' : 3,'RED':4,'BLUE':5,'GRAY':6,'WHITE':7,'BLACK':8}
arr = [[] for _ in range(9)]


for i in range(9):
    shape, sp_cr,bg = map(str, input().split())
    arr[i].append(dic[shape])
    arr[i].append(dic[sp_cr])
    arr[i].append(dic[bg])

N = int(input())
combi = []
visit = [0]*9
check = []
recur(0,0)
length = len(check) # 총 가능한 길이
answer = 0
gule = False
check_combi = [0]*length # 해당 배열을 불렀는지 확인

for c in range(N):
    a = input()

    if len(a) == 1:
        if 0 not in check_combi and not gule:
            answer += 3
            gule = True
        else:
            answer -= 1

    else:
        # 합!
        h,shape,color,back =a.split()
        hh = [int(shape)-1,int(color)-1,int(back)-1]
        hh.sort()
        if hh in check:
            idx = check.index(hh)
            if check_combi[idx] == 0:
                answer += 1
                check_combi[idx] = 1
            else:
                answer -= 1
        else:
            answer -= 1
print(answer)


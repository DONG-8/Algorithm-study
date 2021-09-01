# 알람시계

H, M = map(int, input().split())

newM = M -45

if newM > 0:
    print(H,newM)
elif newM < 0:
    MM  = 60+newM
    HH = H-1
    if HH < 0:
        HH = 23
    print(HH, MM)
elif newM==0:
    print(H, 0)
else:    
    pass


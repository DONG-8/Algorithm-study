
A = int(input())
B = int(input())
C = int(input())

a = {
    "0" : 0,
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0,
    "6" : 0,
    "7" : 0,
    "8" : 0,
    "9" : 0
}

titi = A*B*C
stst = str(titi)
for i in stst:
    a[i] += 1
for key, value in a.items():
    print(value)
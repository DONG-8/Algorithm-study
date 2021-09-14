'''
주차

13 24 42 89

76 152

'''

T = int(input())

for t in range(T):
    N = int(input())

    park = list(map(int, input().split()))

    park.sort()

    print((park[-1]-park[0])*2)

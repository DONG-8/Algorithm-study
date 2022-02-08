string = input()
num_list = list(map(str, range(10)))
result = []
for i in string:
    if i in num_list:
        print(i,end='')

    
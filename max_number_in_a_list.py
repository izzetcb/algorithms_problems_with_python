list = [3, 1, 5, 7, 2, 6]

max_number = list[0]

for i in range(1,len(list)):
    if(max_number < list[i]):
        max_number = list[i]

print(max_number)
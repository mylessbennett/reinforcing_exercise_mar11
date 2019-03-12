my_dict = {}

for num in range(1, 51):
    my_dict[num] = num
print(my_dict)

for i, num in my_dict.items():
    if num % 2 == 0 and num % 7 == 0:
        my_dict[i] = num * 2
    elif num % 2 == 0:
        my_dict[i] = num + 1
    elif num % 7 == 0:
        my_dict[i] = num - 1
    else:
        my_dict[i] = num

print(my_dict)

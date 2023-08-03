def find_minimum(numbers):
    min_num = numbers[0]
    for i in numbers:
        if i < min_num:
            min_num = i
    return min_num

my_list = [17, 5, 9, 12, 2]
minimum_number = find_minimum(my_list)
print(minimum_number)
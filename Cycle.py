my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5, ]
zero = 0
while zero <= len(my_list): # пробовал с "while True" - тоже работает
    number = my_list[zero]
    if number > 0 :
        print(number)
    elif number < 0 :
        break
    zero  += 1

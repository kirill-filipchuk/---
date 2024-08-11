first = input("введите число 1: ")
second = input("введите число 2: ")
third =  input("введите число 3: ")
if first != second and second != third and third != first:
    print(0)
if first == second and second == third:
    print(3)
elif first == second or second == third or third == first:
    print(2)
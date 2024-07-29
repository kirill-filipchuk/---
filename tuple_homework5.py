immutable_var = 1, "Kirill" ,False
print(immutable_var)  # выполнение кортежа
#immutable_var[0:] = 2,3,4,5
#print(immutable_var)   #попытка изменения
#  изменить элементы не получается так как tuple это неизменяемый тип данных
mutable_list = [1, 2, 3, "Kirill", True ]
print(mutable_list) # Вывод списка
mutable_list[0:] = 6,9,3, "Andre", False # Изменение элементов списка
print(mutable_list)
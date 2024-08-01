my_dict = {"Kirill": 24_08_2001, "Max" : 26_08_2003, "Sergey" : 13_10_1999 }
print(my_dict)
print(my_dict.get("Kirill")) # существующий ключ
print(my_dict.get("Piter")) # отсутствующий ключ
my_dict.update({"Stas" : 25_01_1980 ,
                "Misha" : 15_09_1999}) # + 2 пары
print(my_dict)
del my_dict["Stas"] # - 1 пара
print(my_dict) # вывод
#---------------------------------------
my_set = 3.14159265 , "Archimedes" , True , 3.14159265 , "Archimedes"
my_list = set(my_set)
print(my_list) # уникальные значения
my_list.update(["Denis" , (1,2,3)]) # +2 значения
print(my_list)
my_list.discard(3.14159265) # - 1 значение
print(my_list) # вывод









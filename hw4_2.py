
entered_list = input("Введите список чисел, разделенных пробелом: ").split()
num_list = [int(i) for i in entered_list]
print(num_list)
lst_number = [x for x in num_list if x > 0]
import math
result1 = math.prod(lst_number)
print(result1)

# можливо можна було зробити простіше, але всі інші версії коду в мене не працювали :(
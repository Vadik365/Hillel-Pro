# 1. Рядки (Strings):
# Напишіть функцію, яка приймає рядок і повертає його довжину.
# Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.

def len_string(text):
    return len(text)
    


def add_strings(str1, str2):
    return str(str1) + str(str2)

# 2. Числа (Int/float):
# Реалізуйте функцію, яка приймає число і повертає його квадрат.
# Створіть функцію, яка приймає два числа і повертає їхню суму.
# Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає чілу частину і залишок.

def quad_num(num):
    return num ** 2
        
    
def sum_nums(num1, num2):
    return num1 + num2
    
def div_nums(num1, num2):
    return num1 // num2, num1 % num2

# 3. Списки (Lists):
# Напишіть функцію для обчислення середнього значення списку чисел.
# Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків.
def avrg_num(nums):
    return sum(nums) / len(nums)  

def get_common_elemnts(list1, list2):
    return list(set(list1) & set(list2))

# 4. Словники (Dictionaries):
# Створіть функцію, яка приймає словник і виводить всі ключі цього словника.
# Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.
def prnt_key(dct):
    for key in dct:
        print(key)

def sum_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)   
    return result

# 5. Множини (Sets):
# Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.
# Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.
def union_sets(set1, set2):
    return set1.union(set2)

def is_subset(set1, set2):
    return set1.issubset(set2)

# 6. Умовні вирази та цикли:
# Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.
# Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.
def check_even_or_odd(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")

def get_even_nums(nums):
    result = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result

# 7. Написати лямбда-функцію визначальну парне/непарне.
# Функція приймає параметр (число) і якщо парне, видає слово “парне”, якщо ні - то “не парне”.
check_even_odd = lambda x: "even" if x % 2 == 0 else "odd"





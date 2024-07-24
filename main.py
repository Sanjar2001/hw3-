# def get_initials(surname, name, patronymic=""):
#   """
#   Функция принимает фамилию, имя и отчество (необязательно)
#   и возвращает инициалы в формате "Фамилия И.О." или "Фамилия И.".
#   """
#   if patronymic:
#     return f"{surname} {name[0]}.{patronymic[0]}."
#   else:
#     return f"{surname} {name[0]}."

# # Получение данных от пользователя
# input_data = input().split()

# # Вызов функции get_initials с полученными данными
# initials = get_initials(*input_data)

# # Вывод инициалов
# print(initials)


# def get_initials(*args):
#   """
#   Функция принимает любое количество аргументов (частей имени) 
#   и возвращает инициалы в формате "Имя И.И.И.".
#   """
#   initials = args[0] + " " + "".join([part[0] + "." for part in args[1:]])
#   return initials

# # Получение данных от пользователя
# full_name = input()
# name_parts = full_name.split()

# # Вызов функции get_initials с полученным именем
# initials = get_initials(*name_parts)

# # Вывод инициалов
# print(initials)


# students = [
#     {"id": 367673, "full_name": "Ярцев Валерий Рустэмович"},
#     {"id": 563234, "full_name": "Шиптенко Виталий Программирович"},
#     {"id": 982123, "full_name": "Датабейзов Иван Джетлагович"},
# ]

# def get_licence(student_id):
#     for student in students:
#         if student["id"] == student_id:
#             return True
#     return False

# id = int(input('Write down an id: '))
# print(get_licence(id))

# OUR_DATA = []
# def fibonachchi(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         formula =fibonachchi(n - 1) + fibonachchi(n - 2) 
#         return formula

# quantity = int(input('How many numbers? '))
# for i in range(quantity):
#     taking = int(input('Write down a number'))
#     result = fibonachchi(taking)
#     OUR_DATA.append(result)
   
# print(*OUR_DATA)


# def decorator_func(fibon):
#     our_data = {}
#     def changer(n):
#         if n not in our_data:
#             our_data[n] = fibon(n)
#         return our_data[n]
#     return changer


# @decorator_func
# def fibonachchi(n):
#     if n == 0:
#         return 0 
#     elif n == 1:
#         return 1
#     else:
#         formula =fibonachchi(n - 1) + fibonachchi(n - 2) 
#         return formula

# n = int(input('How many numbers: '))
# results = []

# for _ in range(n):
#     k = int(input('Write down a number: '))
#     results.append(fibonachchi(k))

# for result in results:
#     print(result)







# Списки Индексы и срезы. Встроенные функции к наборам элементов.
# Списковое включение List comprehension.
# Кортежи

# numbers = ('word', True, 34, 56.1)
# print(type(numbers))
# <class 'tuple'>

# numbers = [23, 7, 10, 5, 2.5, 2.5]
# print(len(numbers))
# print(sum(numbers))
# print(min(numbers))
# print(max(numbers))
# Вывод
# 6
# 50.0
# 2.5
# 23


# students = ['nuralym', 'esentur', 'kairat', 'emir', 'tilek', 'akyl', 'anna']
# students_2 = [name.title() for name in students if 'a' not in name]
# print(students)
# print(students_2)


# students_copy = students.copy
# students[0] = 'tom'
# print(id(students))
# print(id(students_copy))
# print(students == students_copy)
# print(students is students_copy)
# print(students)
# print(students_copy)

"""delette"""
# students.remove('emir')
# delete = students.pop(0)
# print(students)
# del students[1:3]
# print(delete)
"""add"""
# students.append('adina')
# students.insert(1, 'kudratila')
# students.insert(1, 'Hello')
# students.extend(["danil", "saadat"])
"""edit"""
# students[-1]= 'akel'
# students[0] = 'abdurahim'
# students.sort()
# students.reverse()

"""индекс"""
# print(students[0])
# print(students[3])
# print(students[-1])

"""срезы"""
# схема среезов - [start:stop:step]
# print(students[1:3])
# print(students[-2:])
# print(students[:2])

# print (type(students))


# Mon = int(input())
# Tue = int(input())
# Wed = int(input())
# Thu = int(input())
# Fri = int(input())
# Sat = int(input())
# Sun = int(input())
days = []
i = 0

while i < 7:
    day = int(input(f'Введите расход за {i + 1} день: '))

    days.append(day)
    i += 1


summ = sum(days)

print("Общая сумма расходов за неделю:", summ)
print("Средний расход за неделю:", round((summ) / 7, 1))


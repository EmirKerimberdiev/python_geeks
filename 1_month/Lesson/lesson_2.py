# time = input("enter time: ").lower()
#
# if time == "morning" or time == "утро":
#     print("good morning")
# elif time == "day" or time == "день":
#     print("good afternoon")
# elif time == "evening" or time == "вечер":
#     print("good evening")
# else:
#     print("время неизвестно, просто здраствуйте.")

#
# temperature = int(input('введите температуру: '))
#
# if -20 <= temperature <= 0:
#     print ('ХОЛОДНО')
# elif temperature <= 1 and temperature <= 15:
#     print ('ПРОХЛАДНО')
# elif temperature >= 16 and  temperature <= 25:
#     print ("ТЕПЛО")
# elif temperature >= 26 and temperature <= 40:
#     print ('ЖАРА')
# else:
#     print(f"несовместимая с жизнью температура {temperature} градусов!!!")
#

Mon = int(input())
Tue = int(input())
Wed = int(input())
Thu = int(input())
Fri = int(input())
Sat = int(input())
Sun = int(input())

summ = Mon + Tue + Wed + Thu + Fri + Sat + Sun

if summ >= 1 and summ <= 500:
    print('мало')
elif summ >= 501 and summ <= 700:
    print('среднее')
elif summ > 701:
    print("много")
else:
    print("ничего не потрачено")

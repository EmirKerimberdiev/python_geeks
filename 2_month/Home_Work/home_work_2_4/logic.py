from random import randint
from decouple import config

start = int(config('start'))
end = int(config('end'))
initial_balance = int(config('initial_capital'))

def logic():

    global initial_balance
    secret = randint(start, end)
    print('Добро пожаловать на игру "Угадай число"!')
    print("Я загадал число от", start, "до", end)
    print(f'Ваш баланс {initial_balance}')

    while initial_balance > 0:
        print("На какую цифру вы хотите поставить ставку ?")
        syfra = int(input())
        if syfra < start or syfra > end:
            print("Неверный ввод")
            break

        print("Введите сколько вы хотите поставить на эту цифру ?")
        suma = int(input())
        if suma > initial_balance or suma < 1:
            print("Неверный ввод")
            break

        if syfra == secret:
            print(f"Поздравляю! Вы угадали число: {secret} и получили {suma} баллов\n")
            initial_balance += suma
        else:
            print(f"К сожалению, вы не угадали число: {secret} и потеряли {suma} баллов\n")
            initial_balance -= suma

        if initial_balance > 0:
            play = input(f'Хотите ли вы поставить еще ставку? Ваш баланс {initial_balance}.\n(yes/q)')
            if play == 'yes':
                continue
            elif play == 'q':
                break
        else:
            print("У вас закончились баллы.")

    print("\nИгра завершена. Поздравляем! Ваш баланс:", initial_balance)

if __name__ == '__main__':
    logic()

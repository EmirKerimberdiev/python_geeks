def calculate(num1: float, operator: str, num2: float) -> float:
    """
    Это обычный калькулятор.

    Параметры:
    num1 (float): Первое число.
    operator (str): Арифметический оператор (+, -, *, /, //, %, **).
    num2 (float): Второе число.

    Возвращает:
    float: Результат арифметической операции.

    Исключения:
    Если num1 или num2 будут делится на 0.
    Если num1 или num2 не являются числами.
    """
    try:
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0 or num1 == 0:
                print("Деление на ноль невозможно.")
            return num1 / num2
        elif operator == "//":
            if num2 == 0 or num1 == 0:
                print("Деление на ноль невозможно.")
            return num1 // num2
        elif operator == "%":
            if num2 == 0 or num1 == 0:
                print("Деление на ноль невозможно.")
            return num1 % num2
        elif operator == "**":
            return num1 ** num2
        else:
            print("Это не оператор. Используйтечто то из этих: +, -, *, /, //, %, **.")
    except:
        print("Параметры num1 и num2 должны быть числами.")


num_1 = float(input("Введите первую переменную: "))
op = str(input("Введите операцию которую вы хотите использовать (+, -, *, /, //, %, **): "))
num_2 = float(input("Ведите вторую переменную: "))

result = calculate(num_1, op, num_2)
print(result)  #

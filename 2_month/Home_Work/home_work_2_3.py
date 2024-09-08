class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    def get_cpu(self):
        return self.__cpu

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def get_memory(self):
        return self.__memory

    def set_memory(self, memory):
        self.__memory = memory

    def make_computations(self, cpu, memory):
        return self.__cpu + self.__memory

    def __eq__(self, other):
        """Оператор == (равно)"""
        if isinstance(other, Computer):
            return self.__memory == other.__memory
        return False

    def __ne__(self, other):
        """Оператор != (не равно)"""
        return not self.__eq__(other)

    def __lt__(self, other):
        """Оператор < (меньше)"""
        if isinstance(other, Computer):
            return self.__memory < other.__memory
        return False

    def __le__(self, other):
        """Оператор <= (меньше или равно)"""
        if isinstance(other, Computer):
            return self.__memory <= other.__memory
        return False

    def __gt__(self, other):
        """Оператор > (больше)"""
        if isinstance(other, Computer):
            return self.__memory > other.__memory
        return False

    def __ge__(self, other):
        """Оператор >= (больше или равно)"""
        if isinstance(other, Computer):
            return self.__memory >= other.__memory
        return False

    def __str__(self):
        return f"Процессор: {self.__cpu}, Оперативная память: {self.__memory}"


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def get_sim_cards_list(self):
        return self.__sim_cards_list

    def set_sim_cards_list(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    def call(self, sim_card_number, call_to_number):
        if sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            print(f"Идет звонок на номер {call_to_number} с сим-карты -{sim_card_number}- {sim_card}")
        else:
            print("Неверный номер сим-карты")

    def __str__(self):
        return f"Список сим-карт: {self.__sim_cards_list}"


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        return print(f"Построение маршрута до {location}")

    def __str__(self):
        return f"Процессор: {self.get_cpu()}, Оперативная память: {self.get_memory()}, Сим-карта: {self.get_sim_cards_list()}"


computer = Computer(2, 4)
print(computer)

phone = Phone(["Beeline", "O!"])
print(phone.call(1, "+996 754 12 35 46"))
print(phone.call(3, "+996 754 12 35 46"))
print(phone)

smart_phone = SmartPhone(4, 8, ["MegaCom"])
smart_phone2 = SmartPhone(2, 4, ["Salam"])

print(smart_phone == smart_phone2)
print(smart_phone != smart_phone2)
print(smart_phone < smart_phone2)
print(smart_phone <= smart_phone2)
print(smart_phone > smart_phone2)
print(smart_phone >= smart_phone2)

print(smart_phone)
print(smart_phone.use_gps("Бишкек"))
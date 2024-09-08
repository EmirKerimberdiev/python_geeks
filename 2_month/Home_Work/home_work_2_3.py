class Figure:
    def __init__(self):
        pass

    unit = "cm"

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def get_side_length(self):
        return self.__side_length

    def set_side_length(self, side_length):
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length * 4

    def info(self):
        return f"Square side length: {self.__side_length}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}."


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def get_length(self):
        return self.__length

    def set_length(self, length):
        self.__length = length

    def get_width(self):
        return self.__width

    def set_width(self, width):
        self.__width = width

    def calculate_area(self):
        return self.__width * self.__length

    def info(self):
        return f"Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit}, area: {self.calculate_area()}{Figure.unit}."


square = Square(4)
square1 = Square(7)

rectangle = Rectangle(4, 2)
rectangle1 = Rectangle(9, 5)
rectangle2 = Rectangle(6, 3)

figure_list = [square, square1, rectangle, rectangle1, rectangle2]
for figur in figure_list:
    print(figur.info())



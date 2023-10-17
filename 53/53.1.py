import math


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def getArea(self):
        return math.pi * self.__radius ** 2

    def getCircumference(self):
        return 2 * math.pi * self.__radius



circle = Circle(5)
print("Площадь круга:", circle.getArea())
print("Длина окружности:", circle.getCircumference())
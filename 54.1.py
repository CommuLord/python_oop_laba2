class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def getSquare(self):
        return self.__width * self.__height

    def getPerimeter(self):
        return 2 * (self.__width + self.__height)

    def getRatio(self):
        return self.getSquare() / self.getPerimeter()

rectangle = Rectangle(5, 3)
print("Площадь прямоугольника:", rectangle.getSquare())
print("Периметр прямоугольника:", rectangle.getPerimeter())
print("Отношение площади к периметру:", rectangle.getRatio())
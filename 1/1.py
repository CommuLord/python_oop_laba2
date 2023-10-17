class Car:
    color = None # цвет автомобиля
    fuel = None # количество топлива
    brand = None # марка автомобиля
    weight = None # вес автомобиля

    def go(self):
        # Команда ехать:
        pass


    def turn(self):
        # Команда поворачивать:
        pass


    def stop(self):
        # Команда остановиться:
        pass


    def print_info(self):
        print("Марка:", self.brand)
        print("Цвет:", self.color)
        print("Количество топлива:", self.fuel)
        print("Вес:", self.weight)

myCar = Car()
myCar.color = 'red'

myCar.fuel = 50

myCar.brand = 'Toyota'
myCar.weight = 1500

myCar.print_info()
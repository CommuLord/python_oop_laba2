class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def get_name(self):
        return self.__name

    def get_salary(self):
        return f"{self.__salary} $"

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def set_age(self, age):
        if 0 <= age <= 120:  # Проверка на допустимый возраст
            self.__age = age
        else:
            print("Ошибка: Недопустимый возраст")

employee = Employee("Илья", 12939292992, 99)

employee.set_name("Александр")
employee.set_salary(108235)
employee.set_age(13)

print("Имя:", employee.get_name())
print("Зарплата:", employee.get_salary())
print("Возраст:", employee.get_age())
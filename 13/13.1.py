class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def display_employee_info(self):
        print(f"Имя: {self.__name}")
        print(f"Зарплата: {self.__salary} руб.")
        print(f"Возраст: {self.__age}")

if __name__ == "__main__":
    employee1 = Employee("Илья", 8, 66)
    employee1.display_employee_info()
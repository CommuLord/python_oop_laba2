class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def print_info(self):
        print("Имя:", self.name)
        print("Возраст:", str(self.age))
        print("Зарплата:", str(self.salary), "руб.")

employee = Employee("Илья", 15, 100)


employee.print_info()
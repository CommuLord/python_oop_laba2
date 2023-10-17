class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def print_info(self):
        print("Имя:", self.name)
        print("Зарплата:", str(self.salary), "руб.")

employee = Employee("Илья", 100)


employee.print_info()
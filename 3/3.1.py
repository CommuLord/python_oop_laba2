class Employee:
    name = None
    age = None
    salary = None

    def print_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Зарплата:", self.salary, "руб.")

employee = Employee()
employee.name = "Василий"
employee.age = "24"
employee.salary = "124124"

employee.print_info()
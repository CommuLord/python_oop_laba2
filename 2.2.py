class Employee:
    name = None

    def print_info(self):
        print("Имя:", self.name)

employee = Employee()
employee.name = "Василий"

employee.print_info()
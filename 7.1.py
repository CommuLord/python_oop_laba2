class Employee:
    name = None

    def nami(self):
        print("Имя:", self.name)

employee = Employee()
employee.name = "Василий"

employee.nami()

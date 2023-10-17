class User:
    name = None

    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


class Employee(User):
    position = None
    department = None

    def __init__(self, name, position, department):
        super().__init__(name)
        self.position = position
        self.department = department

    def getPosition(self):
        return self.position

    def getDepartment(self):
        return self.department



employee = Employee("Илья Гусевин", "Писатель", "Редакция журнала")


print(employee.getName())


print(employee.getPosition())
print(employee.getDepartment())
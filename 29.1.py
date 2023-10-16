class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name


class Employee(User):
    position = None
    department = None

    def setPosition(self, position):
        self.position = position

    def setDepartment(self, department):
        self.department = department


# Создаем объект класса Employee
employee = Employee()
employee.setName("Гураня Гусев")
employee.setPosition("Учитель")
employee.setDepartment("ВКСИИТ")

name = employee.getName()
print(name)

position = employee.position
department = employee.department
print(position)
print(department)
class Employee:
    name = None
    salary = None
    last_name = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setLastName(self, last_name):
        self.last_name = last_name

    def getLastName(self):
        return self.last_name


# Создаем объект класса Employee
employee = Employee()
employee.setName("Илья")
employee.setSalary(5234003240)
employee.setLastName("Гусёк")

# Используем методы класса Employee
name = employee.getName()
salary = employee.getSalary()
last_name = employee.getLastName()

print(name, salary, last_name)
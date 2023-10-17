class Employee:
    name = None
    salary = None

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeesCollection:
    employees = []

    def add(self, employee):
        self.employees.append(employee)

    def show(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Salary: {employee.salary}")

    def calculateTotalSalary(self):
        totalSalary = 0
        for employee in self.employees:
            totalSalary += employee.salary
        return totalSalary

    def calculateAverageSalary(self):
        if len(self.employees) > 0:
            totalSalary = self.calculateTotalSalary()
            averageSalary = totalSalary / len(self.employees)
            return averageSalary
        else:
            return 0


employeesCollection = EmployeesCollection()

employeesCollection.add(Employee("Алексей", 500))
employeesCollection.add(Employee("Гусевин", 6000213))
employeesCollection.add(Employee("Александ", 7123000))

employeesCollection.show()

totalSalary = employeesCollection.calculateTotalSalary()
print(f"Итого: {totalSalary} руб.")

averageSalary = employeesCollection.calculateAverageSalary()
print(f"Средняя зарплата: {averageSalary} руб.")
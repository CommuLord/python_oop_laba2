class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_name(self):
        return self.name
    def get_salary(self):
        return self.salary
    def increase_salary(self):
        self.salary *= 1.1

employee = Employee("Илья", 1007)

print("Имя:", employee.get_name())
print("Зарплата:", employee.get_salary())

employee.increase_salary()

# Проверяем новую зарплату
print("Новая зарплата:", employee.get_salary())
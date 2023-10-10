class Employee:
    name = None
    age = None
    salary = None

    def print_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Зарплата:", self.salary, "руб.")

# Создаем первого сотрудника
employee1 = Employee()
employee1.name = "Василий"
employee1.age = "24"
employee1.salary = "69000"
employee1.print_info()

# Создаем второго сотрудника
employee2 = Employee()
employee2.name = "Олег"
employee2.age = "30"
employee2.salary = "130000"
employee2.print_info()

total_salary = int(employee1.salary) + int(employee2.salary)
print("Общая зарплата:", total_salary, "руб.")
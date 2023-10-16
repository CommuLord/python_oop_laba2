class Employee:
    name = None
    salary = None

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


employees = [
    Employee("Илья", 5000),
    Employee("Влад", 6000),
    Employee("Андрей", 7000)
]


for employee in employees:
    print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

class Employee:
    age = None

    def setAge(self, age):
        if 18 <= age <= 65:
            self.age = age
        else:
            raise ValueError("Неправильный возраст. Должен быть введён от 18 до 65.")

    def getAge(self):
        return self.age

employee = Employee()
age = employee.getAge()

try:
    employee.setAge(70)  # Выбросит исключение ValueError
except ValueError as e:
    print(e)


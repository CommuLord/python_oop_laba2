class User:
    def setAge(self, age):
        if age >= 0:
            self.age = age
        else:
            raise Exception('Нужно больше 0')

class Employee(User):
    def setAge(self, age):
        if age <= 120:
            super().setAge(age)  # вызов метода родителя
        else:
            raise Exception('Нужно меньше 120')
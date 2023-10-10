class Student:
    name = None
    age = None
    salary = None

    def print_info(self):
        print("Имя:", self.name)
        print("Возраст:", self.age)
        print("Зарплата:", self.salary, "руб.")

student = Student()
student.name = "Василий"
student.age = "24"
student.salary = "124124"

student.print_info()
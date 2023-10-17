class Employee:

    salary = None
    def salari(self):
        print("Зарплата:", self.salary, "руб.")

employee = Employee()
employee.salary = "124124"

employee.salari()
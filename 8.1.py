class Student:
    name = None
    surname = None

    def cap_name(self):
        if self.name:
            self.name = self.name[0].upper() + self.name[1:]
            self.surname = self.surname[0].upper() + self.surname[1:]

    def print_info(self):
        print("имя:", self.name)
        print("возраст:", self.surname)

    def get_initials(self):
        initials = ""
        if self.name:
            initials += self.name[0]
        if self.surname:
            initials += self.surname[0]
        return initials.upper()

student = Student()
student.name = "илья"
student.surname = "гусев"

student.cap_name()
student.get_initials()
initials = student.get_initials()
print("инициалы:", initials)
student.print_info()
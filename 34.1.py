class User:
    def setName(self, name):
        self.name = name

    def getName(self):
        return self._capeFirst(self.name)

    def _capeFirst(self, stri):
        return stri.capitalize()


class Employee(User):
    def setAge(self, age):
        self.age = age

    def getAge(self):
        return self.age

    def getFormattedName(self):
        return self._capeFirst(self.name)


employee = Employee()
employee.setName("Илья")
employee.setAge(30)

print(employee.getName())
print(employee.getAge())
print(employee.getFormattedName())
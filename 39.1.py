class User:
    def setName(self, name):
        self._name = name

    def getName(self):
        return self._name


class Employee(User):
    def setEmployeeId(self, employee_id):
        self._employee_id = employee_id

    def getEmployeeId(self):
        return self._employee_id


class Programmer(Employee):
    def setProgrammingLanguage(self, language):
        self._programming_language = language

    def getProgrammingLanguage(self):
        return self._programming_language


class Designer(Employee):
    def setDesignTool(self, tool):
        self._design_tool = tool

    def getDesignTool(self):
        return self._design_tool



programmer = Programmer()
programmer.setName('Джо')
programmer.setEmployeeId(123)
programmer.setProgrammingLanguage('Python')

designer = Designer()
designer.setName('Кирилл')
designer.setEmployeeId(456)
designer.setDesignTool('Photoshop')

print(programmer.getName())
print(programmer.getEmployeeId())
print(programmer.getProgrammingLanguage())

print(designer.getName())
print(designer.getEmployeeId())
print(designer.getDesignTool())
class Position:
    name = None

    def __init__(self, name):
        self.name = name

class Department:
    name = None

    def __init__(self, name):
        self.name = name

class User:
    name = None
    position = None
    department = None

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department

# Создаем объекты отдельных классов
position = Position("Феминист")
department = Department("Отдел продаж")

# Создаем объект пользователя с передачей объектов второго и третьего параметров
user = User("Илья Гусев", position, department)

# Выводим имя, должность и отдел для созданного работника
print(user.name)
print(user.position.name)
print(user.department.name)
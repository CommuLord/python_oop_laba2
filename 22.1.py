import re

class Validator:
    def isEmail(self, string):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(pattern, string):
            return True
        else:
            return False

    def isDomain(self, string):
        pattern = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, string):
            return True
        else:
            return False

    def isNumber(self, string):
        if string.isdigit():
            return True
        else:
            return False

validator = Validator()

# Проверка строки на корректный email
email = "test@example.com"
isValidEmail = validator.isEmail(email)
print(isValidEmail)  # Вывод: True

# Проверка строки на корректное имя домена
domain = "example.com"
isValidDomain = validator.isDomain(domain)
print(isValidDomain)  # Вывод: True

# Проверка строки на содержание только чисел
number = "12345"
isOnlyNumbers = validator.isNumber(number)
print(isOnlyNumbers)  # Вывод: True
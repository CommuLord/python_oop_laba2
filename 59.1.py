import calendar


class Month:
    def __init__(self, month_number):
        self.month_number = month_number

    def get_month_number(self):
        return self.month_number

    def get_month_name(self):
        month_names = [
            'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
        ]
        return month_names[self.month_number - 1]

    def get_last_day_number(self):
        _, last_day = calendar.monthrange(2023, self.month_number)
        return last_day

    def get_first_weekday_number(self):
        first_day_weekday = calendar.weekday(2023, self.month_number, 1)
        return first_day_weekday

    def get_last_weekday_number(self):
        last_day = self.get_last_day_number()
        last_day_weekday = calendar.weekday(2023, self.month_number, last_day)
        return last_day_weekday


month = Month(10)

month_number = month.get_month_number()
print(f"Номер месяца: {month_number}")

month_name = month.get_month_name()
print(f"Название месяца: {month_name}")

last_day_number = month.get_last_day_number()
print(f"Номер последнего дня месяца: {last_day_number}")

first_weekday_number = month.get_first_weekday_number()
print(f"Номер дня недели первого дня месяца: {first_weekday_number}")

last_weekday_number = month.get_last_weekday_number()
print(f"Номер дня недели последнего дня месяца: {last_weekday_number}")
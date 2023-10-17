from datetime import datetime, timedelta


class Zate:
    def __init__(self, year, month, day):
        self.date = datetime(year, month, day)

    def get_year(self):
        return self.date.year

    def get_month(self):
        return self.date.month

    def get_day(self):
        return self.date.day

    def get_weekday_number(self):
        return self.date.weekday()

    def get_weekday_name(self):
        weekday_names = [
            'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'
        ]
        weekday_number = self.get_weekday_number()
        return weekday_names[weekday_number]

    def get_month_name(self):
        month_names = [
            'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
            'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'
        ]
        month_number = self.get_month()
        return month_names[month_number - 1]


class ZateExt(Zate):
    def add_years(self, years):
        new_date = self.date + timedelta(days=years * 365)
        return new_date

    def subtract_years(self, years):
        new_date = self.date - timedelta(days=years * 365)
        return new_date

    def add_months(self, months):
        new_date = self.date + timedelta(
            days=months * 30)  # Приближенное значение, исходя из предположения о 30 днях в месяце
        return new_date

    def subtract_months(self, months):
        new_date = self.date - timedelta(
            days=months * 30)  # Приближенное значение, исходя из предположения о 30 днях в месяце
        return new_date

    def add_days(self, days):
        new_date = self.date + timedelta(days=days)
        return new_date

    def subtract_days(self, days):
        new_date = self.date - timedelta(days=days)
        return new_date


date = ZateExt(2023, 10, 16)

new_date = date.add_years(2)
print(f"Дата после добавления 2 лет: {new_date}")

new_date = date.subtract_years(1)
print(f"Дата после вычитания 1 года: {new_date}")

new_date = date.add_months(6)
print(f"Дата после добавления 6 месяцев: {new_date}")

new_date = date.subtract_months(3)
print(f"Дата после вычитания 3 месяцев: {new_date}")

new_date = date.add_days(15)
print(f"Дата после добавления 15 дней: {new_date}")

new_date = date.subtract_days(7)
print(f"Дата после вычитания 7 дней: {new_date}")
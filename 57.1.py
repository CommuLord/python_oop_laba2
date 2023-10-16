from datetime import datetime


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
            'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
        ]
        weekday_number = self.get_weekday_number()
        return weekday_names[weekday_number]

    def get_month_name(self):
        month_names = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]
        month_number = self.get_month()
        return month_names[month_number - 1]


date = Zate(2023, 10, 16)

year = date.get_year()
month = date.get_month()
day = date.get_day()
weekday_number = date.get_weekday_number()
weekday_name = date.get_weekday_name()
month_name = date.get_month_name()

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Weekday Number: {weekday_number}")
print(f"Weekday Name: {weekday_name}")
print(f"Month Name: {month_name}")
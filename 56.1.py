from datetime import datetime


class Period:
    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def get_seconds_difference(self):
        seconds = (self.end_time - self.start_time).total_seconds()
        return int(seconds)

    def get_minutes_difference(self):
        minutes = (self.end_time - self.start_time).total_seconds() // 60
        return int(minutes)

    def get_hours_difference(self):
        hours = (self.end_time - self.start_time).total_seconds() // 3600
        return int(hours)

    def get_days_difference(self):
        days = (self.end_time - self.start_time).days
        return int(days)


start_time = datetime(2023, 1, 1, 0, 0, 0)
end_time = datetime.now()

period = Period(start_time, end_time)

seconds_diff = period.get_seconds_difference()
minutes_diff = period.get_minutes_difference()
hours_diff = period.get_hours_difference()
days_diff = period.get_days_difference()

print(f"Seconds difference: {seconds_diff}")
print(f"Minutes difference: {minutes_diff}")
print(f"Hours difference: {hours_diff}")
print(f"Days difference: {days_diff}")
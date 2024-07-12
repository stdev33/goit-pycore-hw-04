from datetime import datetime


def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        today = datetime.today()
        delta = today - input_date
        return delta.days
    except ValueError:
        return "Invalid date format. Please, use format 'YYYY-MM-DD'."


print(get_days_from_today("2020-10-09"))
print(get_days_from_today("2024-07-08"))
print(get_days_from_today("test_invalid_date_format"))

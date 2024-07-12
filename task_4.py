from datetime import datetime, timedelta


def get_upcoming_birthdays(users):
    today = datetime.today().date()
    end_date = today + timedelta(days=7)

    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= end_date:
            if birthday_this_year.weekday() >= 5:
                birthday_this_year += timedelta(days=(7 - birthday_this_year.weekday()))

            upcoming_birthdays.append(
                dict(name=user["name"], congratulation_date=birthday_this_year.strftime("%Y.%m.%d")))

    return upcoming_birthdays


users_birthdays = [
    {"name": "Alice", "birthday": "1990.07.01"},
    {"name": "Bob", "birthday": "1985.07.04"},
    {"name": "Charlie", "birthday": "1992.07.06"},
    {"name": "David", "birthday": "1980.07.08"},
    {"name": "Eve", "birthday": "1995.07.10"},
]

print("Список привітань на цьому тижні:", get_upcoming_birthdays(users_birthdays))

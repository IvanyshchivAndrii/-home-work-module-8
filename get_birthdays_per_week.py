from datetime import datetime

users = ({'name': 'Dima', 'birthday': datetime(year=1993, month=6, day=25)},
         {'name': 'Anton', 'birthday': datetime(year=1993, month=6, day=3)},
         {'name': 'Den', 'birthday': datetime(year=1993, month=6, day=4)},
         {'name': 'Pavlo', 'birthday': datetime(year=1993, month=6, day=5)},
         {'name': 'Oleg', 'birthday': datetime(year=1993, month=3, day=24)},
         {'name': 'Ira', 'birthday': datetime(year=1993, month=6, day=8)})

current = datetime.now()


def get_birthdays_per_week(users: list):
    birthday_people = {}
    current_date = datetime.now()

    for user in users:
        if current_date.month == user['birthday'].month and abs(current_date.day - user['birthday'].day) <= 7:
            if not birthday_people or datetime(current_date.year, current_date.month, user['birthday'].day).strftime('%A') not in list(birthday_people):
                birthday_people[datetime(current_date.year, current_date.month, user['birthday'].day).strftime('%A')] = [user['name']]
            else:
                birthday_people[datetime(current_date.year, current_date.month, user['birthday'].day).strftime('%A')].append(user['name'])

    if 'Monday' in list(birthday_people):
        birthday_people['Monday'] += (birthday_people.pop('Saturday', []) + birthday_people.pop('Sunday', []))
    else:
        birthday_people['Monday'] = (birthday_people.pop('Saturday', []) + birthday_people.pop('Sunday', []))

    for k, i in birthday_people.items():
        print(f'{k}: {", ".join(i)}')






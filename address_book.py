from collections import UserDict
from datetime import date, timedelta, datetime

class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def get_upcoming_birthdays(self, days=7):
        upcoming = []
        today = date.today()

        for record in self.data.values():
            if record.birthday is None:
                continue

            bd = record.birthday.value  # datetime
            birthday_this_year = datetime.strptime(bd, "%d.%m.%Y").replace(year=today.year).date()

            if birthday_this_year < today:
                birthday_this_year = birthday_this_year.replace(year=today.year + 1)

            # Перенесення на будній день, якщо день народження на вихідний
            if birthday_this_year.weekday() >= 5:
                days_ahead = 0 - birthday_this_year.weekday() + 7
                birthday_this_year += timedelta(days=days_ahead)

            # Якщо день народження у найближчі дні
            if 0 <= (birthday_this_year - today).days <= days:
                upcoming.append({
                    "name": record.name.value,
                    "birthday": birthday_this_year.strftime("%d.%m.%Y")
                    })

        return upcoming

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())
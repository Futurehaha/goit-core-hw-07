from datetime import datetime

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def __init__(self, value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Phone number must contain exactly 10 digits")
        super().__init__(value)

class Birthday(Field):
    def __init__(self, value):
        # Якщо передали рядок, намагаємося перетворити на об'єкт datetime
        if isinstance(value, str):
            try:
                value = datetime.strptime(value, "%d.%m.%Y")
            except ValueError:
                raise ValueError("Invalid date format. Use DD.MM.YYYY")
        # Перевіряємо якщо вже передали об'єкт datetime
        elif not isinstance(value, datetime):
            raise TypeError("Birthday must be a string or datetime object")

        super().__init__(value)
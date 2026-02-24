from fields import Name, Phone, Birthday

class Record:
    def __init__(self, name, birthday = None):
        self.name = Name(name)
        self.phones = []

        if birthday is not None:
            self.birthday = Birthday(birthday)
        else:
            self.birthday = None

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    def remove_phone(self, phone):
        found_phone = self.find_phone(phone)
        if found_phone:
            self.phones.remove(found_phone)
            return
        raise ValueError("Phone not found")
    
    def edit_phone(self, old_phone, new_phone):
        phone_obj = self.find_phone(old_phone)
        if phone_obj:
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
            return
        raise ValueError("Old phone not found")
    
    def find_phone(self, phone):
        for phone_in_lst in self.phones:
            if phone_in_lst.value == phone:
                return phone_in_lst
        return None

    def __str__(self):
        phones_str = ", ".join(phone.value for phone in self.phones)

        if self.birthday:
            birthday_str = self.birthday
        else:
            birthday_str = "Birthday not added"

        return f"Name: {self.name.value}, Phones: {phones_str}, Birthday: {birthday_str}"
from record import Record
from address_book import AddressBook
from utils import input_error


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        record = Record(name)
        book.add_record(record)
    record.add_birthday(birthday)
    return f"Birthday added for {name}."

@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    return f"{name}'s birthday: {record.birthday.value}"

@input_error
def birthdays(args, book: AddressBook):
    upcoming = book.get_upcoming_birthdays(days=7)
    if not upcoming:
        return "No upcoming birthdays in the next 7 days."
    return "\n".join(f"{item['name']} - {item['birthday']}" for item in upcoming)

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message

@input_error
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone, *_ = args
    record = book.find(name)
    record.edit_phone(old_phone, new_phone)
    return f"Phone updated for {name}."

@input_error
def show_phone(args, book: AddressBook):
    name, *_ = args
    record = book.find(name)
    return "; ".join(phone.value for phone in record.phones)
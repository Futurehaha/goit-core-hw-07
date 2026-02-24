from functools import wraps

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__

        messages = {
            "add_contact": "Usage: add <name> <phone>\nUse only digits and 10 digits in the number.",
            "change_phone": "Usage: change <name> <old_phone> <new_phone>\nUse only digits and 10 digits in the number.",
            "add_birthday": "Usage: add-birthday <name> <DD.MM.YYYY>",
            "show_birthday": "Usage: show-birthday <name>",
            "show_phone": "Usage: phone <name>",
        }

        try:
            return func(*args, **kwargs)

        except IndexError:
            return messages.get(func_name, "Not enough arguments provided.")

        except AttributeError:
            return "Contact not found."

        except ValueError:
            return messages.get(func_name, "Invalid value provided.")
        
        except Exception:
            return "An unexpected error occurred."

    return wrapper
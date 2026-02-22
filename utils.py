from functools import wraps

def input_error(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (ValueError, TypeError, IndexError) as e:
            return f"Error: {e}"
    return wrapper
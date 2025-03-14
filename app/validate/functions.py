from uuid import UUID


def check_passport(passport: str):
    
    try:
        int(passport)
    except ValueError:
        raise ValueError("Invalid passport, it must contain only digits")
    
    return passport
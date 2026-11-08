import re
def validate_email(emil):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, emil):
        raise  ValueError (f'Invaild email: {emil}')
    return True
def validate_age(age):
    if not isinstance(age,int):
        raise TypeError("Age must be an integer")
    if age <0 or age > 150:
        raise  ValueError("Age must be 0-150")
    return  True

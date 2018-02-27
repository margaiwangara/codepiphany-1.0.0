import re

#validate email
def validate_email(email):
    if re.search("^[a-zA-Z0-9.\%-_]+\@[a-zA-Z0-9_.-]+\.[a-zA-Z]{2,5}$",email):
        return email
    return None

#validate password
def password_validate(password):
    if re.search("^(?=[-_a-zA-Z0-9]*?[A-Z])(?=[-_a-zA-Z0-9]*?[a-z])(?=[-_a-zA-Z0-9]*?[0-9])\S{8,}$",password):
        return password
    return None

#check password is same
def password_match(password,confirm):
    if password_validate(password) is not None:
        if password == confirm:
            return password
    return None

#username validation
def username_validation(username):
    if re.search("^(?=[-_a-zA-Z0-9]*?[A-Z])(?=[-_a-zA-Z0-9]*?[a-z])(?=[-_a-zA-Z0-9]*?[0-9])\S{8,}$",username):
        return username
    return None

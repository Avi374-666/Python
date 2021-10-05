def login_up(user, passw):
    if check_string(user) and check_string(passw):
        if check_pass(passw):
            return True
        else:
            return False
    return False


def check_string(x):
    if type(x) == str:
        return True
    else:
        return False


def check_pass(y):
    special = ['@', '#', '$', '%']
    out = True

    if len(y) < 8:
        out = False

    if any(char.isdigit() for char in y):
        out = True

    if any(char.isupper() for char in y):
        out = True

    if any(char.isupper() for char in y):
        out = True

    if any(char in special for char in y):
        out = True

    return out

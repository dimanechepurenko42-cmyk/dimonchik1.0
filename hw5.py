def is_strong_password(password):
    has_digit = False
    has_upper = False
    has_lower = False
    special_count = 0
    special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    for char in password:
        if char.isdigit():
            has_digit = True
        if char.isupper():
            has_upper = True
        if char.islower():
            has_lower = True
        if char in special_chars:
            special_count += 1

            if has_digit and has_upper and has_lower and special_count >= 2:
                return True

    return False
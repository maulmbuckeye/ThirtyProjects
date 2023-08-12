
def check_password(possible_password: str) -> bool:
    try:
        with open("passwords.text") as file:
            unacceptable_passwords: list[str] = file.read().splitlines()
    except Exception as _:
        unacceptable_passwords = ["password", "passwd", "mike_ulm"]
    if possible_password in unacceptable_passwords:
        return False
    return True


def request_and_check_password():
    ...


if __name__ == '__main__':
    request_and_check_password()

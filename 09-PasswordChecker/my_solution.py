
def check_password(possible_password: str) -> bool:
    unacceptable_passwords = ["password", "passwd"]
    if possible_password in unacceptable_passwords:
        return False
    return True


def request_and_check_password():
    ...


if __name__ == '__main__':
    request_and_check_password()

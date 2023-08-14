# Class based password checker
#
# This comment mainly added to test rebasing

class PasswordResult:

    def __init__(self, result: bool, msg=''):
        self._result = result
        self._msg = msg

    def __bool__(self) -> bool:
        return self._result


class BadPasswords:

    def __init__(self, bad_passwords: list[str]):
        self._bad = bad_passwords

    def is_ok(self, a_candidate: str) -> bool:
        return a_candidate in self._bad

    def is_ok_and_rank(self, a_candidate: str) -> tuple[bool, str]:
        for i, common_password in enumerate(self._bad, start=1):
            if a_candidate == common_password:
                return False, str(i)
        return True, ''


def password_check(possible_password: str,
                   list_of_bad: str = "passwords.text") -> PasswordResult:
    """Return (True, '') if password is okay,
    otherwise return (False, "reason").

    Reasons include:
        '3' -> 3rd on bad password list
    """
    try:
        with open(list_of_bad) as file:
            bp = BadPasswords(file.read().splitlines())
    except Exception as _:
        bp = BadPasswords(["password", "passwd", "mike_ulm"])
    return PasswordResult(*bp.is_ok_and_rank(possible_password))



def request_and_check_password():
    ...


if __name__ == '__main__':
    request_and_check_password()

class PasswordResult:

    def __init__(self, result: bool, *, msg=None, rank=None, password=None):
        self._result = result
        self.msg = msg
        self.rank = rank
        self._password = password

    def __bool__(self) -> bool:
        return self._result

    @property
    def password(self):
        return self._password

    def __str__(self):
        return_str = ""
        if self._password:
            return_str = f"{self._password}: "
        return_str += "✅" if self else "❌"
        return_str += f" (#{self.rank})" if self.rank else ""
        return return_str


class BadPasswords:

    def __init__(self, bad_passwords: list[str]):
        self._bad = bad_passwords

    def is_ok(self, a_candidate: str) -> bool:
        return a_candidate in self._bad

    def is_ok_and_rank(self, a_candidate: str) -> PasswordResult:
        for i, common_password in enumerate(self._bad, start=1):
            if a_candidate == common_password:
                return PasswordResult(False,
                                      password=a_candidate,
                                      msg="Commonly used password",
                                      rank=i)
        return PasswordResult(True, password=a_candidate)


def password_check(possible_password: str,
                   list_of_bad: str = "passwords.text") -> PasswordResult:
    """Return PasswordResult"""

    try:
        with open(list_of_bad) as file:
            bp = BadPasswords(file.read().splitlines())
    except Exception as _:
        bp = BadPasswords(["password", "passwd", "mike_ulm"])
    return bp.is_ok_and_rank(possible_password)


def request_and_check_password():
    ...


if __name__ == '__main__':
    request_and_check_password()

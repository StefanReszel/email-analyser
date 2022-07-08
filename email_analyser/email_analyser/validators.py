import re


class EmailValidator:
    def __init__(self):
        self._pattern = r"^[^@\s]+@[^@\s]+\.[\dA-ZA-Za-z]{1,4}$"

    def validate(self, email: str) -> bool:
        is_valid = re.match(self._pattern, email)

        if is_valid:
            return True
        return False

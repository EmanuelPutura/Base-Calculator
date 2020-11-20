from colors.color import Color


class UserCommandError(Exception):
    def __str__(self):
        return Color.FAIL + super().__str__() + Color.ENDC


class ValidationError(Exception):
    def __str__(self):
        return Color.FAIL + super().__str__() + Color.ENDC
from errors.exceptions import ValidationError


class IntegerValidator:
    def __init__(self):
        self.__digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    def validate_base(self, base):
        """
        Validates a given base
        :param base: a string representing a base
        :return: -
        :exception: ValidationError if the base is not a correct one
        """
        # a string representing all the errors
        errors = ''
        if not base.isdigit():
            errors += "'{}' is not a valid base.\n".format(base)
        if not len(errors):
            base = int(base)  # we can now safely convert base to an integer
            if base < 2 or base > 16:
                errors += 'Base must be a positive integer between 2 and 16.\n'
        if len(errors):
            raise ValidationError(errors)

    def validate_integer(self, integer, base):
        """
        Validates a positive integer in a given base
        :param integer: an Integer object
        :param base: a given base
        :return: -
        :exception: ValidationError if the integer is not a correct one
        """
        # a string representing all the errors
        errors = ''
        # the list of accepted digits in the given base
        base_digits = self.__digits[:base]
        for digit in integer.number:
            if digit not in base_digits:
                errors += "'{}' is not a valid digit in base {}.\n".format(digit, base)
        if len(errors):
            raise ValidationError(errors)

    def validate_mul(self, operand2):
        """
        Validates second operand of a mul operation
        :param operand2: an integer object representing the second operand of a mul operation
        :return: -
        :exception: ValidationError if the second operand is not a correct one
        """
        if len(operand2.number) != 1:
            raise ValidationError('Multiplication can only be done by one digit.\n')

    def validate_div(self, operand2):
        """
        Validates second operand of a div operation
        :param operand2: an integer object representing the second operand of a div operation
        :return: -
        :exception: ValidationError if the second operand is not a correct one
        """
        errors = ''
        if len(operand2.number) != 1:
            errors += 'Division can only be done by one digit.\n'
        if operand2.number == '0':
            errors += 'Dividing by zero is not accepted.\n'
        if len(errors):
            raise ValidationError(errors)

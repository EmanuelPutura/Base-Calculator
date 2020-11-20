from domain.integer import Integer


class IntegerService:
    """
    The service class for integers
    """
    def __init__(self, integer_validator):
        self.__integer_validator = integer_validator

    def add(self, first_operand, second_operand, base):
        """
        Adds two integers in a given base
        :param first_operand: the string representation of the first integer
        :param second_operand: the string representation of the second integer
        :param base: a given base
        :return: -
        """
        # the first operand will always be the number with more digits (if their number of digits is different)
        if len(first_operand) < len(second_operand):
            first_operand, second_operand = second_operand, first_operand
        self.__integer_validator.validate_base(base)
        base = int(base)
        integer1 = Integer(first_operand, base)
        self.__integer_validator.validate_integer(integer1, base)
        integer2 = Integer(second_operand, base)
        self.__integer_validator.validate_integer(integer2, base)

    def sub(self, first_operand, second_operand, base):
        """
        Subtracts two integers in a given base
        :param first_operand: the string representation of the first integer
        :param second_operand: the string representation of the second integer
        :param base: a given base
        :return: -
        """
        # the first operand will always be the number with more digits (if their number of digits is different)
        if len(first_operand) < len(second_operand):
            first_operand, second_operand = second_operand, first_operand
        self.__integer_validator.validate_base(base)
        base = int(base)
        integer1 = Integer(first_operand, base)
        self.__integer_validator.validate_integer(integer1, base)
        integer2 = Integer(second_operand, base)
        self.__integer_validator.validate_integer(integer2, base)

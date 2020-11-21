from domain.integer import Integer


class IntegerService:
    """
    The service class for integers
    """
    def __init__(self, integer_validator):
        self.__integer_validator = integer_validator

    def operation_prepare_data(self, base, first_operand, second_operand):
        """
        Gets some user data from console module, validates it and transforms it into domain module entities
        :param base: a given base
        :param first_operand: a given operand
        :param second_operand: a given operand
        :return: two integers representing the two operands of a certain operation
        """
        self.__integer_validator.validate_base(base)
        base = int(base)  # now we can safely convert the base to an integer
        integer1 = Integer(first_operand, base)
        self.__integer_validator.validate_integer(integer1, base)
        integer2 = Integer(second_operand, base)
        self.__integer_validator.validate_integer(integer2, base)
        return integer1, integer2

    def add(self, first_operand, second_operand, base):
        """
        Adds two integers in a given base
        :param first_operand: the string representation of the first integer
        :param second_operand: the string representation of the second integer
        :param base: a given base
        :return: the result of the addition
        """
        integer1, integer2 = self.operation_prepare_data(base, first_operand, second_operand)
        return integer1 + integer2

    def sub(self, first_operand, second_operand, base):
        """
        Subtracts two integers in a given base
        :param first_operand: the string representation of the first integer
        :param second_operand: the string representation of the second integer
        :param base: a given base
        :return: the result of the subtraction
        """
        integer1, integer2 = self.operation_prepare_data(base, first_operand, second_operand)
        return integer1 - integer2

    def mul(self, first_operand, second_operand, base):
        """
        Multiplies two integers in a given base
        :param first_operand: the string representation of the first integer
        :param second_operand: the string representation of the second integer
        :param base: a given base
        :return: the result of the multiplication
        """
        integer1, integer2 = self.operation_prepare_data(base, first_operand, second_operand)
        self.__integer_validator.validate_mul(integer2)
        return integer1 * integer2

    def div(self, first_operand, second_operand, base):
        """
        Divides two integers in a given base
        :param first_operand: the string representation of the first integer
        :param second_operand: the string representation of the second integer
        :param base: a given base
        :return: the result of the division
        """
        integer1, integer2 = self.operation_prepare_data(base, first_operand, second_operand)
        self.__integer_validator.validate_div(integer2)
        return integer1 / integer2, integer1 % integer2

    def convert(self, source_base, destination_base, integer):
        self.__integer_validator.validate_base(source_base)
        source_base = int(source_base)  # now we can safely convert the source base to an integer
        self.__integer_validator.validate_base(destination_base)
        destination_base = int(destination_base)  # now we can safely convert the destination base to an integer
        integer = Integer(integer, source_base)
        self.__integer_validator.validate_integer(integer, source_base)
        integer.convert_to_base(destination_base)
        return integer

from colors.color import Color


class Integer:
    def __init__(self, number, base):
        self.__number = number
        self.__base = base
        self.__corresponding_digit = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

    @property
    def number(self):
        return self.__number

    @property
    def base(self):
        return self.__base

    def __len__(self):
        return len(self.__number)

    def __add__(self, other):
        """
        Overloading the '+' operator
        :param other: the second operator of the addition
        :return: the sum of the two operands
        """
        base = self.__base
        first_operand = self.__number
        second_operand = other.number
        result = ''

        # if the number of digits of the two operands differs, then the first_operand will always have more digits
        if len(first_operand) < len(second_operand):
            first_operand, second_operand = second_operand, first_operand
        length_delta = len(first_operand) - len(second_operand)
        # now the number of digits of the two operands will be the same
        second_operand = '0' * length_delta + second_operand
        length = len(first_operand)
        # for every digit in the two operands
        carry = 0
        for i in reversed(range(length)):
            sum = carry + self.__corresponding_digit[first_operand[i]] + self.__corresponding_digit[second_operand[i]]
            digit = sum % base
            carry = sum // base
            result += str(digit)
        if carry:
            result += str(carry)
        return Integer(result[::-1], base)

    def __sub__(self, other):
        """
        Overloading the '-' operator
        :param other: the second operator of the subtraction
        :return: the difference of the two operands
        """
        pass

    def __str__(self):
        return self.__number

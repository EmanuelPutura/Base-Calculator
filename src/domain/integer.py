class Integer:
    """
    Abstract data type representing an integer written in a certain base
    """
    def __init__(self, number, base):
        self.__number = number
        self.__base = base
        self.__corresponding_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
                               '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
        # this is basically the inverse dictionary of the one above
        self.__corresponding_digit = dict(map(reversed, self.__corresponding_number.items()))

    @property
    def number(self):
        return self.__number

    @property
    def base(self):
        return self.__base

    def convert_into_base(self, destination_base):
        pass

    def substitution_method(self, destination_base):
        pass

    def successive_divisions_method(self, destination_base):
        pass

    def convert_to_base10(self):
        """
        Converts the integer into base 10
        :return: -
        """
        number = self.__number
        source_base = self.__base
        destination_base = 10
        result = 0

        power = 1
        # for every digit of the number (reverse order)
        for i in reversed(range(len(number))):
            digit = self.__corresponding_number[number[i]]
            result += digit * power
            power *= source_base
        self.__number = str(result)
        self.__base = destination_base

    def convert_from_base10(self, destination_base):
        """
        Converts the integer from base 10 into a given destination base
        :param destination_base: a given destination base
        :return: -
        """
        # we can convert the number to int as we know it is written in base 10
        number = int(self.__number)
        source_base = self.__base
        result = ''

        while number != 0:
            result = self.__corresponding_digit[number % destination_base] + result
            number //= destination_base
        self.__number = result
        self.__base = destination_base

    def rapid_conversions(self, destination_base):
        pass

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
        carry = 0
        # for every digit in the two operands
        for i in reversed(range(length)):
            sum = carry + self.__corresponding_number[first_operand[i]] + self.__corresponding_number[second_operand[i]]
            digit = sum % base
            carry = sum // base
            result += self.__corresponding_digit[digit]
        if carry:
            result += str(carry)
        return Integer(result[::-1], base)

    def __sub__(self, other):
        """
        Overloading the '-' operator
        :param other: the second operator of the subtraction
        :return: the difference of the two operands
        """
        base = self.__base
        first_operand = self.__number
        second_operand = other.number
        result = ''

        length_delta = len(first_operand) - len(second_operand)
        # now the number of digits of the two operands will be the same
        if length_delta > 0:
            second_operand = '0' * length_delta + second_operand
        length = len(first_operand)
        carry = 0
        # for every digit in the two operands
        for i in reversed(range(length)):
            difference = self.__corresponding_number[first_operand[i]] - self.__corresponding_number[second_operand[i]] - carry
            carry = 0
            if difference < 0:
                carry = 1
                difference += base
            result += self.__corresponding_digit[difference]
        return Integer(result.rstrip('0')[::-1], base)

    def __mul__(self, other):
        """
        Overloading the '*' operator. Works only for multiplication of a number with a digit.
        :param other: the second operator of the multiplication
        :return: the product of the two operands
        """
        base = self.__base
        first_operand = self.__number
        second_operand = other.number
        result = ''

        # if the number of digits of the two operands differs, then the first_operand will always have more digits
        if len(first_operand) < len(second_operand):  # so now we shall know that the second operand is a digit
            first_operand, second_operand = second_operand, first_operand
        length = len(first_operand)
        carry = 0
        # for every digit in the two operands
        for i in reversed(range(length)):
            product = self.__corresponding_number[first_operand[i]] * self.__corresponding_number[second_operand] + carry
            digit = product % base
            carry = product // base
            result += self.__corresponding_digit[digit]
        if carry:
            result += str(carry)
        return Integer(result[::-1], base)

    def __truediv__(self, other):
        """
        Overloading the '/' operator. Works only for dividing a number by a digit.
        :param other: the second operator of the division
        :return: the division of the two operands
        """
        base = self.__base
        first_operand = self.__number
        second_operand = other.number
        result = ''

        length = len(first_operand)
        carry = 0
        # for every digit in the two operands
        for i in range(length):
            print(first_operand[i])

    def __eq__(self, other):
        """
        Checks if two integers in a given base are equal. The integers must be written in the same base.
        :param other: the second operand
        :return: True if they are equal, False else
        """
        return self.__number == other.number and self.__base == other.base

    def __str__(self):
        """
        :return: the string representation of an integer
        """
        return self.__number

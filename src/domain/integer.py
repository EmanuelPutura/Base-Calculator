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

    @number.setter
    def number(self, other):
        self.__number = other

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, other):
        self.__base = other

    @staticmethod
    def find_exponent(base, number):
        """
        Finds the exponent of base such that base^exponent = number. If such a number does not exist, the
        function returns None
        :param base: a given base
        :param number: a given number
        :return: the exponent of base such that base^exponent = number. If such a number does not exist, the
        function returns None
        """
        exponent = 0
        while number != 1:
            if number % base != 0:
                return None
            number //= base
            exponent += 1
        return exponent

    def convert_to_base(self, destination_base):
        """
        Converts the integer to another base. Depending on the base, a certain conversion method is chosen
        :param destination_base: the destination base
        :return: -
        """
        if self.__base == destination_base:  # the source base is the same with the destination base
            return
        if self.__base == 2 and destination_base in [4, 8, 16] or self.__base == 4 and destination_base == 16:
            self.rapid_conversions_less(destination_base)
        elif destination_base == 2 and self.__base in [4, 8, 16] or destination_base == 4 and self.__base == 16:
            self.rapid_conversions_greater(destination_base)
        elif self.__base < destination_base:
            self.substitution_method(destination_base)
        else:
            self.successive_divisions_method(destination_base)

    def convert_to_base_using_base10(self, destination_base):
        """
        Converts the integer to another base, using base 10 as an intermediate base
        :param destination_base: the destination base
        :return: -
        """
        self.convert_to_base10()
        self.convert_from_base10(destination_base)

    def substitution_method(self, destination_base):
        """
        Converts the integer to another base, using the substitution method. Note that we use this method in
        this application only if the source base is less than the destination base
        :param destination_base: the destination base
        :return: -
        """
        power = Integer('1', destination_base)
        converted_source_base = Integer(str(self.__corresponding_digit[self.__base]), destination_base)
        result = Integer('0', destination_base)
        for i in reversed(range(len(self.__number))):
            digit = Integer(self.__number[i], destination_base)
            result = result + power * digit
            power = power * converted_source_base
        self.__number = result.number
        self.__base = result.base

    def successive_divisions_method(self, destination_base):
        """
        Converts the integer to another base, using the successive divisions method. Note that we use this method in
        this application only if the source base is greater than the destination base
        :param destination_base: the destination base
        :return: -
        """
        result = ''
        remainder = Integer('0', self.__base)
        converted_destination_base = Integer(self.__corresponding_digit[destination_base], self.__base)
        while self.__number != '0':
            remainder.assign_value(self % converted_destination_base)
            self.assign_value(self / converted_destination_base)
            result = remainder.number + result
        if result == '':
            result = '0'
        self.__number = result
        self.__base = destination_base

    def rapid_conversions_less(self, destination_base):
        """
        Converts the integer to another base, using the rapid conversions method. Note that we use this method in
        this application only if the destination base is a power of the source base and also the source base is a power
        of two
        :param destination_base: the destination base
        :return:
        """
        digits_group_length = self.find_exponent(self.__base, destination_base)
        result = ''
        # in order to be able to form groups of digits
        while len(self.__number) % digits_group_length != 0:
            self.__number = '0' + self.__number

        for i in range(len(self.__number) // digits_group_length):
            group = Integer(self.__number[-digits_group_length:], self.__base)
            group.substitution_method(destination_base)
            result = group.number + result
            self.number = self.__number[:-digits_group_length]

        if result == '':
            result = '0'
        self.__number = result.lstrip('0')
        self.__base = destination_base

    def rapid_conversions_greater(self, destination_base):
        """
        Converts the integer to another base, using the rapid conversions method. Note that we use this method in
        this application only if the source base is a power of the destination base and also the destination base is
        a power of two
        :param destination_base: the destination base
        :return:
        """
        digits_group_length = self.find_exponent(destination_base, self.__base)
        result = ''

        for i in reversed(range(len(self.__number))):
            group = Integer(self.__number[i], self.__base)

            group.successive_divisions_method(destination_base)
            while len(group.number) < digits_group_length:
                group.number = '0' + group.number
            result = group.number + result

        if result == '':
            result = '0'
        self.__number = result.lstrip('0')
        self.__base = destination_base

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
        result = ''

        while number != 0:
            result = self.__corresponding_digit[number % destination_base] + result
            number //= destination_base
        if result != '':
            self.__number = result
        self.__base = destination_base

    def get_division_results(self, other):
        base = self.__base
        first_operand = self.__number
        second_operand = other.number
        result = ''
        length = len(first_operand)
        remainder = 0
        # for every digit in the two operands
        for i in range(length):
            digit = Integer(first_operand[i], base)
            digit.convert_to_base10()
            base10_digit = int(digit.number) + remainder * base
            digit = Integer(str(base10_digit // self.__corresponding_number[second_operand]), 10)
            digit.convert_from_base10(base)
            digit = digit.number
            result += digit
            remainder = base10_digit % self.__corresponding_number[second_operand]
        result_integer = Integer(result.lstrip('0'), base)
        if result_integer.number == '':
            result_integer.number = '0'
        remainder = Integer(str(self.__corresponding_digit[remainder]), base)
        if remainder.number == '':
            remainder.number = '0'
        return remainder, result_integer

    def assign_value(self, other):
        """
        Reassigns an integer
        :param other: the new integer
        :return: -
        """
        self.__number = other.number
        self.__base = other.base

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
        result_integer = Integer(result.rstrip('0')[::-1], base)
        if result_integer.__number == '':
            result_integer.__number = '0'
        return result_integer

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
        result_integer = Integer(result.rstrip('0')[::-1], base)
        if result_integer.__number == '':
            result_integer.__number = '0'
        return result_integer

    def __truediv__(self, other):
        """
        Overloading the '/' operator. Works only for dividing a number by a digit.
        :param other: the second operator of the division
        :return: the division of the two operands
        """
        remainder, result_integer = self.get_division_results(other)
        return result_integer

    def __mod__(self, other):
        """
        Overloading the '%' operator. Works only for dividing a number by a digit.
        :param other: the second operator of the division
        :return: the remainder of the division of two operands
        """
        remainder, result_integer = self.get_division_results(other)
        return remainder

    def __len__(self):
        """
        :return: the number of digits of an integer given in a certain base
        """
        return len(self.__number)

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
        return self.__number if self.__number != '' else '0'

from colors.color import Color
from errors.exceptions import UserCommandError, ValidationError


class Console:
    def __init__(self, integer_service):
        self.__integer_service = integer_service

    def ui_add(self):
        base = input(Color.OKGREEN + 'Please input a base: ').strip()
        first_operand = input('Please input the first operand: ').strip()
        second_operand = input('Please input the second operand: ').strip()
        result = self.__integer_service.add(first_operand, second_operand, base)
        print('{} + {} = {} (in base {})\n'.format(first_operand, second_operand, result, base) + Color.ENDC)

    def ui_sub(self):
        base = input(Color.OKGREEN + 'Please input a base: ').strip()
        first_operand = input('Please input the first operand: ').strip()
        second_operand = input('Please input the second operand: ').strip()
        result = self.__integer_service.sub(first_operand, second_operand, base)
        print('{} - {} = {} (in base {})\n'.format(first_operand, second_operand, result, base) + Color.ENDC)

    def ui_mul(self):
        base = input(Color.OKGREEN + 'Please input a base: ').strip()
        first_operand = input('Please input the first operand: ').strip()
        second_operand = input('Please input the second operand: ').strip()
        result = self.__integer_service.mul(first_operand, second_operand, base)
        print('{} * {} = {} (in base {})\n'.format(first_operand, second_operand, result, base) + Color.ENDC)

    def ui_div(self):
        base = input(Color.OKGREEN + 'Please input a base: ').strip()
        first_operand = input('Please input the first operand: ').strip()
        second_operand = input('Please input the second operand: ').strip()
        result = self.__integer_service.div(first_operand, second_operand, base)
        print('{} / {} = {}, remained = {} (in base {})\n'.format(first_operand, second_operand, result[0], result[1], base) + Color.ENDC)

    def ui_convert(self):
        source_base = input(Color.OKGREEN + 'Please input a source base: ').strip()
        integer = input("Please input a positive integer in base '{}': ".format(source_base)).strip()
        destination_base = input('Please input a destination base: ').strip()
        result = self.__integer_service.convert(source_base, destination_base, integer)
        print('{}({}) = {}({})\n'.format(integer, source_base, result, destination_base) + Color.ENDC)

    @staticmethod
    def __print_menu():
        full_title_number_of_characters = 67
        title = ' Base Calculator and Converter Application '
        margins_length = (full_title_number_of_characters - len(title)) // 2

        print(Color.OKCYAN + '*' * margins_length + title + '*' * margins_length)
        print(Color.OKBLUE + ' add - add two positive integers in a given base')
        print(' sub - subtract two positive integers in a given base')
        print(' mul - multiply two positive integers in a given base')
        print(' div - divide one positive integer by a digit in a given base')
        print(' convert - convert a positive integer from one base to another')
        print(' exit - exit the application')
        print(Color.OKCYAN + '*' * full_title_number_of_characters + Color.ENDC + '\n')

    def run(self):
        commands = {'add': self.ui_add, 'sub': self.ui_sub, 'mul': self.ui_mul, 'div': self.ui_div, 'convert': self.ui_convert}

        while True:
            try:
                self.__print_menu()
                command = input('>> ').strip()
                if command == 'exit':
                    return
                if command not in commands:
                    raise UserCommandError("'{}' is not a valid command.".format(command))
                commands[command]()
            except UserCommandError as userCommandError:
                print(userCommandError)
            except ValidationError as validationError:
                print(validationError)
            except Exception as exception:
                print(Color.FAIL + 'Unexpected error occurred.\n' + str(exception) + Color.ENDC)

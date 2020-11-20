from colors.color import Color
from errors.exceptions import UserCommandError, ValidationError


class Console:
    def __init__(self, integer_service):
        self.__integer_service = integer_service

    def ui_add(self):
        base = input('Please input base: ')
        first_operand = input('Please input the first operand: ')
        second_operand = input('Please input the second operand: ')
        self.__integer_service.add(first_operand, second_operand, base)

    def ui_sub(self):
        base = input('Please input base: ')
        first_operand = input('Please input the first operand: ')
        second_operand = input('Please input the second operand: ')
        self.__integer_service.sub(first_operand, second_operand, base)

    def ui_div(self):
        pass

    def ui_mul(self):
        pass

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
        print(' exit - exit the application')
        print(Color.OKCYAN + '*' * full_title_number_of_characters + Color.ENDC)

    def run(self):
        commands = {'add': self.ui_add, 'sub': self.ui_sub, 'mul': self.ui_div, 'div': self.ui_mul}

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

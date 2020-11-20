class Integer:
    def __init__(self, number, base):
        self.__number = number
        self.__base = base

    @property
    def number(self):
        return self.__number

    @property
    def base(self):
        return self.__base

    def __len__(self):
        return len(self.__number)

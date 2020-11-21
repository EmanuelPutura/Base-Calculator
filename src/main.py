"""
    @author: Emanuel-Vasile Puțura
    @start_date: 20.11.2020
    @finish_date: 21.11.2020

    The application must implement algorithms for:
    -	arithmetic operations for positive integers: addition, subtraction, multiplication and division by one digit,
        in a base p from {2,3,...,9,10,16}
    -	conversions of natural numbers between two bases p,q from {2,3,...,9,10,16} using the substitution method or
        successive divisions and rapid conversions between two bases p,q from {2, 4, 8, 16}.
    The application must have a menu such that all operations and conversion methods to be verified separately.

"""
from presentation.console import Console
from services.integer_service import IntegerService
from validation.integer_validator import IntegerValidator

if __name__ == "__main__":
    integer_validator = IntegerValidator()
    integer_service = IntegerService(integer_validator)
    console = Console(integer_service)
    console.run()

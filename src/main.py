from presentation.console import Console
from services.integer_service import IntegerService
from validation.integer_validator import IntegerValidator

if __name__ == "__main__":
    integer_validator = IntegerValidator()
    integer_service = IntegerService(integer_validator)
    console = Console(integer_service)
    console.run()

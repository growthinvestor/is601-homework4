import pytest
from main import calculate_and_print  # Ensure this import matches your project structure

@pytest.mark.parametrize("a_string, b_string, operation_string, expected_string", [
    ("5", "3", 'add', "The result of 5 add 3 is equal to 8"),
    ("10", "2", 'subtract', "The result of 10 subtract 2 is equal to 8"),
    ("4", "5", 'multiply', "The result of 4 multiply 5 is equal to 20"),
    ("20", "4", 'divide', "The result of 20 divide 4 is equal to 5"),
    ("1", "1", 'divide', "The result of 1 divide 1 is equal to 1"),
    ("1", "0", 'divide', "An error occurred: Cannot divide by zero."),  # Added period
    ("9", "3", 'modulus', "The result of 9 modulus 3 is equal to 0"),
    ("10", "3", 'modulus', "The result of 10 modulus 3 is equal to 1"),
    ("2", "3", 'exponentiate', "The result of 2 exponentiate 3 is equal to 8"),
    ("3", "0", 'exponentiate', "The result of 3 exponentiate 0 is equal to 1"),
    ("9", "3", 'unknown', "Unknown operation: unknown."),  # Added period
    ("a", "3", 'add', "Invalid number input: a or 3 is not a valid number."),  # Added period
    ("5", "b", 'subtract', "Invalid number input: 5 or b is not a valid number.")  # Added period
])

def test_calculate_and_print(a_string, b_string, operation_string, expected_string, capsys):
    calculate_and_print(a_string, b_string, operation_string)
    captured = capsys.readouterr().out.strip().rstrip(".")
    assert captured == expected_string.rstrip(".")


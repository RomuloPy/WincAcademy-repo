from basic_calculator_function import basic_calculator
from faker import Faker

fake = Faker()

def test_basic_calculator():

    number1 = fake.random_number()
    number2 = fake.random_number()
    expect = number1 + number2

    result = basic_calculator(number1, number2, "add")

    assert result == number1 + number2
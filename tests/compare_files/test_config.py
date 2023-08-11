from enum import Enum


# Generated with confluent v0.0.1 (https://pypi.org/project/confluent/).
class TestConfig(any, Enum):
    MY_BOOLEAN = True
    MY_INTEGER = 142
    MY_FLOAT = 322.0
    MY_DOUBLE = 233.9
    MY_REGEX = r'Test Reg(E|e)x'  # Just another RegEx.
    MY_SUBSTITUTED_STRING = 'Sometimes I just want to scream Hello World!'

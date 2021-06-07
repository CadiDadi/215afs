# Create a project fizzbuzz using pycharm IDE.
# Create a Fizzbuzzunittest.py file
# The Fizzbuzz.py file should be able to achieve following tests:
# I can call FizzBuzz
# Get “1” when I pass in 1
# Get “2” when I pass in 2
# In the fizzbuzzunittest.py file, write a code that should achieve above tests through failing test, all the way to refractor. 

import pytest

def FizzBuzz(value):
    return str(value)

def CheckFizzBuzz(value, ExpectedReturnValue):
    ReturnValue = FizzBuzz(value)
    assert ReturnValue == ExpectedReturnValue

def TestReturnsWith1():
    CheckFizzBuzz(1, "1")

def TestReturnWith2():
    CheckFizzBuzz(2, "2")
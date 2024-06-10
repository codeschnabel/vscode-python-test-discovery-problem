import unittest
import sys

print("sys.path: ")
print(sys.path)

from fizzbuzz.fizzbuzzer import FizzBuzzer

class FizzBuzzerTests(unittest.TestCase):

    def test_fizzBuzz_1_returns_1(self):
        fizzBuzzer = FizzBuzzer()

        result = fizzBuzzer.fizzBuzz(1)

        self.assertEqual("1", result)

    def test_fizzBuzz_2_returns_2(self):
        fizzBuzzer = FizzBuzzer()

        result = fizzBuzzer.fizzBuzz(2)

        self.assertEqual("2", result)

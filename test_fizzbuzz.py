from unittest import TestCase
from fizzbuzz import get_fizzbuzz


class FizzbuzzTest(TestCase):
    def setUp(self):
        self.multiples = {3:'Fizz', 5:'Buzz'}

    def test_1_when_1(self):
        self.assertEqual(get_fizzbuzz(self.multiples, 1), '1')

    def test_2_when_2(self):
        self.assertEqual(get_fizzbuzz(self.multiples, 2), '2')

    def test_Fizz_when_3(self):
        self.assertEqual(get_fizzbuzz(self.multiples, 3), 'Fizz')

    def test_4_when_4(self):
        self.assertEqual(get_fizzbuzz(self.multiples, 4), '4')

    def test_Buzz_when_5(self):
        self.assertEqual(get_fizzbuzz(self.multiples, 5), 'Buzz')

    def test_FizzBuzz_when_15(self):
        self.assertEqual(get_fizzbuzz(self.multiples, 15), 'FizzBuzz')

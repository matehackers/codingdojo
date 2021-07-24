import unittest
from fizzBuzz import *

"""
FizzBuzz

Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:

Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
"""


class FizzBuzzTest(unittest.TestCase):

  def test_fizzBuzz_3(self):
    self.assertEqual(fizzBuzz(3), 'Fizz')

  def test_fizzBuzz_2(self):
    self.assertEqual(fizzBuzz(2), 2)

  def test_fizzBuzz_4(self):
    self.assertEqual(fizzBuzz(4), 4)

  def test_fizzBuzz_5(self):
    self.assertEqual(fizzBuzz(5), 'Buzz')

  def test_fizzBuzz_10(self):
    self.assertEqual(fizzBuzz(10), 'Buzz')

  def test_fizzBuzz_6(self):
    self.assertEqual(fizzBuzz(6), 'Fizz')
  
  def test_fizzBuzz_15(self):
    self.assertEqual(fizzBuzz(15), 'FizzBuzz')

  def test_fizzBuzz_16(self):
    self.assertEqual(fizzBuzz(16), 16)

  def test_fizzBuzz_30(self):
    self.assertEqual(fizzBuzz(30), 'FizzBuzz')

  def test_fizzBuzz_150(self):
    self.assertEqual(fizzBuzz(150), 'FizzBuzz')
  

unittest.main()
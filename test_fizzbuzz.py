import fizzbuzz 
import unittest 

class TestFizzBuzz(unittest.TestCase):
    def test_multiple_of_three(self):
        self.assertEqual(fizzbuzz.fizzbuzz(3)[-1], 'Fizz')
        self.assertEqual(fizzbuzz.fizzbuzz(6)[-1], 'Fizz')
        self.assertEqual(fizzbuzz.fizzbuzz(99)[-1], 'Fizz')
        self.assertEqual(fizzbuzz.fizzbuzz(381)[-1], 'Fizz')
        self.assertEqual(fizzbuzz.fizzbuzz(999999)[-1], 'Fizz')

    def test_multiple_of_five(self):
        self.assertEqual(fizzbuzz.fizzbuzz(5)[-1], 'Buzz')
        self.assertEqual(fizzbuzz.fizzbuzz(10)[-1], 'Buzz')
        self.assertEqual(fizzbuzz.fizzbuzz(560)[-1], 'Buzz')
        self.assertEqual(fizzbuzz.fizzbuzz(5095)[-1], 'Buzz')

    def test_multiples_of_three_and_five(self):
        self.assertEqual(fizzbuzz.fizzbuzz(15)[-1], 'FizzBuzz')
        self.assertEqual(fizzbuzz.fizzbuzz(30)[-1], 'FizzBuzz')
        self.assertEqual(fizzbuzz.fizzbuzz(2775)[-1], 'FizzBuzz')

    def test_non_multiples(self):
        self.assertEqual(fizzbuzz.fizzbuzz(0), [])
        self.assertEqual(fizzbuzz.fizzbuzz(2)[-1], 2)
        self.assertEqual(fizzbuzz.fizzbuzz(481)[-1], 481)
        self.assertEqual(fizzbuzz.fizzbuzz(998)[-1], 998)

        

if __name__ == '__main__':
    unittest.main()
    
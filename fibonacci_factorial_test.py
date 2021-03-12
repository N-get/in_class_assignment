import unittest
import factorial
import fibonacci
class factorial1(unittest.TestCase):
    def test_factorial(self):
        for Firstname in range(0, 101):
            self.assertIsInstance(Firstname, int, 'Entry is not of the correct type!')
            factorial.factorial(Firstname)

class fibonacci1(unittest.TestCase):
    def test_fibonacci(self):
        for Firstname1 in range(0, 21):
            self.assertIsInstance(Firstname1, int, 'Entry is not of the correct type!')
            result1 = fibonacci.fibonacci(Firstname1)
            print(result1)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(factorial1('test_factorial'))
    suite.addTest(fibonacci1('test_fibonacci'))
    unittest.TextTestRunner().run(suite)

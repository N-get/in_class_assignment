import unittest
import factorial
import fibonacci
class factorial1(unittest.TestCase):
    def test_factorial(self):
        for Firstname in range(1, 101):
            self.assertIsInstance(Firstname, int, 'Entry is not of the correct type!')
            self.assertTrue(Firstname, 'Entry is blank!')
            factorial.factorial(Firstname)

class fibonacci1(unittest.TestCase):
    def test_fibonacci(self):
        for Firstname1 in range(1, 21):
            self.assertIsInstance(Firstname1, int, 'Entry is not of the correct type!')
            self.assertTrue(Firstname1, 'Entry is blank!')
            result1 = fibonacci.fibonacci(Firstname1)
            print(result1)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(factorial1('test_factorial'))
    suite.addTest(fibonacci1('test_fibonacci'))
    unittest.TextTestRunner().run(suite)

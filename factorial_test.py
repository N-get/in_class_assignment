
import unittest
import factorial
class factorial1(unittest.TestCase):
    def test_factorial(self):
            Firstname = int(input("Input your number!"))
            self.assertIsInstance(Firstname, int, 'Entry is not of the correct type!')
            self.assertTrue(Firstname, 'Entry is blank!')
            factorial.factorial(Firstname)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(factorial1('test_factorial'))

    unittest.TextTestRunner().run(suite)

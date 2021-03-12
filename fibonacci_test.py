
import unittest
import fibonacci
class fibonacci1(unittest.TestCase):
    def test_fibonacci(self):
        for Firstname in range(1, 21):
            self.assertIsInstance(Firstname, int, 'Entry is not of the correct type!')
            self.assertTrue(Firstname, 'Entry is blank!')
            result = fibonacci.fibonacci(Firstname)
            print(result)

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(fibonacci1('test_fibonacci'))

    unittest.TextTestRunner().run(suite)
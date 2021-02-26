
import unittest
def fibonacci(n):
    if (n < 0):
        print("Invalid input!")
    elif(n == 0):
        return 0
    elif(n == 1):
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
def factorial(n):
    if(n == 0):
        return 0
    elif(n < 0):
        print("Invalid input!")
    else:
        for i in range (1, n ):
            n = n * i
        return n

class firstname_lastname(unittest.TestCase):
    
    def test4(self):
        Firstname = int(input("Input your number!"))
        self.assertIsInstance(Firstname, int, 'Entry is not of the correct type!')
        self.assertTrue(Firstname, 'Entry is blank!')
        print(fibonacci(Firstname))
        print(factorial(Firstname))


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(firstname_lastname('test4'))
    
    unittest.TextTestRunner().run(suite)
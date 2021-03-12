
def factorial(n):
    if(n == 0):
        print(0)
        return 0
    elif(n < 0):
        print("Invalid input!")
    else:
        for i in range (1, n ):
            n = n * i
        print(n)
        return n

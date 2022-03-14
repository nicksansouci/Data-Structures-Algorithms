def funcThree():
    print("Three")

def funcTwo():
    funcThree()
    print("Two")

def funcOne():
    funcTwo()
    print("One")

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(factorial(5))
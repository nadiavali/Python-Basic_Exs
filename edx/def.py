
def main():
    name = input('What is your name? ')
    hello(name)

def hello(value):
    print('hello', value)

main()


def main():
    x = int(input('what is x? '))
    print('x squared is', square(x))

def square(n):
    return n**2

main()

# pow power and first is the number and second is power

def main():
    x = int(input('what is x? '))
    print('x squared is', square(x))

def square(n):
    return pow(n, 3)

main()


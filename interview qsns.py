print('Hello, Python!')
print("Hello, Python!")
print('''Hello, Python!''')
print('"Hello, Python"')
print("'Hello, Python'")

# arithmetic operations
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')
print('sum: ', int(num1) + int(num2))
print('sub: ', int(num1) - int(num2))
print('mul: ', int(num1) * int(num2))
print('div: ', float(num1) / float(num2))

maximum = max(int(num1), int(num2))
print("the maximum number is: ", maximum)

# even or odd:
n = int(input('enter a number: '))
if (n % 2) == 0:
    print(f'{n} is even number')
else:
    print(f'{n} is odd number')


def PrimeNumber(n):
    if n>1:
        for i in range(2, int(n/2)+1):
            if n%i==0:
                print(f'{n} is not prime number')
                break
        else:
            print(f'{n} is a prime number')
    else:
        print(f'{n} is not a prime number')

n = int(input('enter a number: '))
PrimeNumber(n)

def factorial(n):
    return(math.factorial(n))
n = int(input('enter a number: '))
print(f'factorial of a number {n} is: ', factorial(n))
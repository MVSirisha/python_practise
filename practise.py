print ('Venkata Sirisha M')
print('O_____')
print('  ||||')
print('*' * 10)
price = 10
print(price)

name = 'John Snow'
age = 20
is_new = True

#taking input
name = input("what is your name?")
print('Hi ' + name)

#type conversion
birth_year = input('Birth year: ')
print(type(birth_year))
age = 2025-int(birth_year)
print(age)
print(type(age))

#string
print('Python for "Beginners"')
print("Python's for Beginners")
print('''Hi John,
Here is our first email to you
Thankyou!
Support team.
''')

course = 'Python for Beginners'
print(course[0])
print(course[-1])
print(course[-2])
print(course[0:])
print(course[ :5])
print(course[ : ])

#copying string
course = 'Python for Beginners'
another=course[:]
print(another)

name = 'Jennifer'
print(name[1:-1])

#formatted strings
first_name = 'John'
last_name = 'Smith'
msg = first_name + '[' + last_name + '] is a coder'
print(msg)
#this above code is correct but not ideal so now we use formatted strings
message = f'{first_name} [{last_name}] is a coder'
print(message)

#string functions
course = 'Python for Beginners'
print(len(course))
print(course.upper())
print(course.find('P'))
print(course.find('Beginners'))
print(course.replace('Beginners', 'Absolute Beginners'))
print('Python' in course)
print('Language' in course)

#arithmetic operations
x=10
print(x)
x=x+3
print(x)
x += 5
print(x)
x -= 2
print(x)
x+= 3*2
print(x)

#math functions
x=2.9
print(round(x))
print(abs(-4.9))

import math
print(math.ceil(2.9))
print(math.floor(2.9))

#if statements
is_hot = False
is_cold = False
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

#logical operators
has_high_income = True
has_good_credit = True
has_criminal_record = False
if has_high_income and has_good_credit:
    print("Eligible for Loan")

if has_high_income or has_good_credit:
    print("Eligible for Loan")

if has_high_income and not has_criminal_record:
    print("Eligible for Loan")

#comparison operator
temp = int(input("what is the temp: "))
if temp > 30:
    print("its a hot day")
else:
    print("its not a hot day")

#project
weight = int(input('weight: '))
unit = (input('(L)bs os(K)g: '))
if unit.upper() == 'L':
    converted = weight * 0.45
    print(f'You are {converted} Kilos')
else:
    converted = weight / 0.45
    print(f'You are {converted} Pounds')

#while loop
i = 1
while i <= 5:
    print(i)
    i = i+1
print("done")

i = 1
while i <= 5:
    print("*" * i)
    i=i+1
print("done")

#car game
command = ''
while True:
    command = input('>').lower()
    if command == 'start':
        print("car started...")
    elif command == 'stop':
        print("car stopped.")
    elif command == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to quit''')
    elif command == 'quit':
        break
    else:
        print("sorry! I don't understand")

#guessing game
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("Yay...You Won!!! :)")
        break
    elif guess_count == guess_limit:
        print('Sorry! you Failed :(')
    else:
        print('Oops! Try again :|')

#for loop
for i in 'python':
    print(i)
print("_____________")
for i in ['Mosh', 'John', 'Sarah', 'Mira']:
    print(i)
print("_____________")
for i in [1,2,3,4]:
    print(i)

#range function
for i in range(10):
    print(i)
print('----------------------')
for i in range(5,10):
    print(i)
print('-------------------------')
for i in range(1,10,2):
    print(i)

#nested loops
for x in range(3):
    for y in range(2):
        print(f'({x}),({y})')

#lists
names = ['Siri', 'Teja', 'Rama', 'Govind']
print(names)
print(names[0])
print(names[1:])
print(names[-1])
print(names[0:2])

#modifying list
names[0] = 'Raja'
print(names)

numbers =[3,6,2,8,4,10]
maximum = numbers[0]
for n in numbers:
    if n>maximum:
        maximum = n
print(maximum)

#2D list
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
print(matrix[0][1])
#modifying
matrix[0][2] = 20
print(matrix[0][2])

for i in matrix:
    for j in i:
        print(j)
#listmethods
n = [5,2,7,4,1]
print(n)
n.append(20)
print(n)
n.insert(0,10)
print(n)
n.remove(5)
print(n)
n.pop()
print(n)
print(n.index(4))
print(50 in n)

n = [5, 2, 1, 5, 7, 4]
print(n)
print(n.count(5))
print(n.sort()) #the sort method doesn't return any value
print(n)
n.reverse()
print(n)
#copy method
n2 = n.copy()
n.append(10)
print(n2)
print(n)

#tuples
n = (1, 2, 3)
print(n[0])
#unpackaging
coords = (1, 2, 3)
x,y,z = coords
print(x)
print(y)
print(z)
#Dictionaries
customer = {
    "name": "John",
    "age": 24,
    "is_verified": True
}
print(customer["name"])
#using get method
print(customer.get("age"))

print(customer.get("birthdate")) #op=none as the key is NA

#supplying values to dictionary
customer["name"] = 'Jack Smith'
customer["birthdate"] = 'Dec 22 1992'
print(customer)

#emoji converter
message = input("<")
words = message.split(' ')
emojis = {
    ":)": "😊",
    ":(": "😕",
    "<3": "❤"
}
output = " "
for word in words:
    output += emojis.get(word, word) + ' '
print(output)

#fuctions
def greet_user():
    print("Hi, there!!!")
    print("Welcome aboard")


print("start")
greet_user()
print("finish")

#parameters
def greet_user(name):
    print(f"Hi, {name}!!!")
    print("Welcome aboard")


print("start")
greet_user("Siri")
print("finish")

def greet_user(first_name, last_name):
    print(f"Hi, {first_name} {last_name}!!!")
    print("Welcome aboard")


print("start")
greet_user('Sirisha', "MV")
print("finish")

#keyword arguments
print('strat')
greet_user(last_name='MV', first_name='Sirisha')
print("finish")


#return statement
def square(n):
    return n*n


print(square(3))


#creating reusable functions
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😕",
        "<3": "❤"
    }
    output = " "
    for word in words:
        output += emojis.get(word, word) + ' '
    return output


message=input('>')
print(emoji_converter(message))

#exception handling
try:
    age = int(input("age: "))
    print(age)
except ValueError:
    print('Invalid Error')
except ZeroDivisionError:
    print('Age cannot be Zero')

#classes
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.y)
point2 = Point()
point2.x = 1
print(point2.x)

#constructor
point = Point()
print(point.x)

#constructor
class Point:
    def __init__(self,x,y):
        self.x = x,
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10,20)
point.x = 11
print(point.x)

#inheritance
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annoying(self):
        print("annoying")

dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.be_annoying()
cat1.walk()

#generating random variables
import random
for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))

mem = ['john', 'smith', 'snow', 'steve']
lead = random.choice(mem)
print(lead)
























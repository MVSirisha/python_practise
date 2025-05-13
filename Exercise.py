#exercise1 - getting input
name = input('What is your name? ')
favourite_color = input('What is your favourite color? ')
print(name + ' likes ' + favourite_color)

#exercise2 - type conversion
weight_lbs = int(input('Weight(lbs): '))
weight_kg = (weight_lbs) * 0.45
print(weight_kg)

#exercise 3 = operators
x = (2+3)*10-3
print(x)

#exercise 4 - if statemnets
price = 1000000
has_good_credit = True
if has_good_credit:
    down_payment = 0.1*price
else:
    down_payment = 0.2*price
print(f"Down payment: ${down_payment}")

#exercise 5 - comparison operators
name = input('name: ')
if len(name) <3:
    print("name should be at least 3 characters")
elif len(name) >50:
    print("name should be maximum of 50 characters")
else:
    print("name looks good!")

#exercise 6 - car game
command = ''
started = False
while True:
    command = input('>').lower()
    if command == 'start':
        if started:
            print("car is already started!")
        else:
            started = True
            print("car started...")
    elif command == 'stop':
        if not started:
            print("car is already stopped!")
        else:
            started = False
            print("car stopped.")
    elif command == 'help':
        print('''start - to start the car
stop - to stop the car
quit - to quit''')
    elif command == 'quit':
        break
    else:
        print("sorry! I don't understand")

#exercise 7 - forloop
prices = [10, 20, 30, 40]
total = 0
for price in prices:
    total += price
print(f'total price: {total}')

#exercise 8 - nested loops
numbers=[5, 2, 5, 2, 2]
for i in numbers:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)

#exercise9:
num = [2,2,4,6,3,4,6,1]
uniques=[]
for n in num:
    if n not in uniques:
        uniques.append(n)
print(uniques)

#exercise 10: dictionaries
phone = input("phone: ")
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
}
output = ''
for n in phone:
    output += digits_mapping.get(n, '!') + ' '
print(output)

#exercise 11: Constructors
class Person:
    def __init__(self,name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


John = Person("John Snow")
John.talk()

Smith = Person("Steve Smith")
Smith.talk()


#exercise 12 - generating random variables
import random
class Dice:
    def roll(self):
        dice1 = random.randint(1,6)
        dice2 = random.randint(1,6)
        return dice1,dice2


dice = Dice()
print(dice.roll())

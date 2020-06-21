print("Good morning world!")
print("It's time for day two of python drills. yay!")
numberOne = 1
addition = 1 + 1
subtraction = 5 - 4
multiplication = 5 * 5
division = 10 / 2
exponentiation = 5 ** 5
numList = list(range(0,15))
print(numList)
puppies = ['puppy', 'doggie', 'stutler', 'good boy', 'poochie']
for puppy in puppies:
    if puppy == 'poochie':
        print(puppy)
    else:
        print("wrong puppy")
length = len(puppies)
messageOne = f"length of puppy list is {length}"
print(messageOne)
boolOne = 'puppy' in puppies
print(boolOne)
boolTwo = 'meow' in puppies
boolThree = 'doggie' in puppies
if 'stutler' in puppies:
    print("Who's a good puppy?")
age = 19
if age == 10:
    age = 11
elif age == 12:
    age = 12
elif age == 15:
    age = 15
else:
    print("do nothing with this age variable. its a drill anyways")
print("okay, now lets play around with dictionaries!")
alien0 = {'color': 'green', 'race': 'blorg', 'weapons': 'none'}
print(alien0['color'])
alien0['armorPoints'] = 50
alien0['damagePoints'] = 3
del alien0['race']



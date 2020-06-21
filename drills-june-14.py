import this
print("Hello world!")
print("These are the drills for June 14th!")
print("Ok that's enough printing of useless strings for now")
message = "Nevermind, not quite done"
print(message)
name = "cameron gott"
print(name.title())
print(name.upper())
print(name.lower())
newMessage = f"{message}  {name}"
print(newMessage)
newerMessage = " {} {} ".format(name, name)
print("\tPython")
whitespace = "   stuff    "
print(whitespace)
print(whitespace.rstrip())
print(whitespace.lstrip())
print(whitespace.strip())
addition = 1 + 2
substraction = 5 - 3
multiplication = 5 * 5
division = 10 / 2
exponent = 5 ** 2
pemdas = 2 + 3 * 4 ** 4
bubble = 0.1 + 0.1
print(bubble)
universe_age = 14_000_000_000
print(universe_age)
x,y,z = 1, 3, 5
PI = 3.14159
#I have nothing to comment here except that at 50 lines I get a cookie
bicycles = ['trike', 'bmx', 'road', 'mountain']
print(bicycles)
print(bicycles[0])
print(bicycles[1])
print(bicycles[2].title())
print(bicycles[3].upper())
bicycles.append('honda')
bicycles.append('haro')
bicycles.append('zionik')
bicycles.append('wheelie')
bicycles.append('red')
bicycles.append('lil tyke')
bicycles.remove('zionik')
print(bicycles)
print("now we sort the list of bicycles. yay!")
bicycles.sort()
print("heres the sorted list of bicycles: ")
print(bicycles)
#god that was a tasty molasses cookie. 
print("god that was a tasty line 50 molasses cookie")
print("now lets reverse this list of weird bicycle names")
bicycles.reverse()
print("ok here it is:")
print(bicycles)
print("ok, how many stupid bicycles do we even have?")
length = len(bicycles)
print(f"ok we have {length} bicycles")
print("wait, whats the last bicycle we added?")
print(f"oh, its {bicycles[-1]}")
print("---------------------")
print("OK lets mess around with some loops and stuff")
for bike in bicycles:
    print(bike)
for value in range(0, 10):
    print(value)
print("lets make some lists using the range function!")
numberList = list(range(0,100))
print(numberList)
evenNumbers = list(range(0,10,2))
print("here's a list of even numbers built with range()")
print(evenNumbers)
newNumberList = list(range(-1, -100, -2))
anotherOne = list(range(100, 0, -1))
print(min(anotherOne))
print(max(anotherOne))
print(sum(anotherOne))
squares = [value**2 for value in range(0,11)]
for bicycle in bicycles:
    if bicycle == 'trike':
        print(bicycle)
    else:
        break
testNum = 1
if testNum == 1:
    break
else:
    break





print("Today's focus is on playing with the standard built-in Python functions")
numList = list(range(-20,0))
print(numList)
for number in numList:
    print(abs(number))
floatList = [0.5, 4.3, -6.6, 3.1]
print(floatList)
for coolerNumber in floatList:
    print(abs(coolerNumber))
print("Now let's test the all(iterable) function.")
print("Should return true for our list of integers:")
print(all(numList))
print(any(numList))
print(any(floatList))
for item in numList:
    print(ascii(item))
for item in floatList:
    print(ascii(item))
print("Hmm, ascii(item) doesn't treat our numbers like objects. Interesting. Totally would in Java.")
for item in numList:
    print(bin(item))
for item in numList:
    print(chr(abs(item)))
print("Hmm, terminal output is blank")
for item in range(0, 500):
    print(chr(item))
print("I wonder if there are dead ranges in the unicode standard, or")
print("if my terminal is unequipped to print them?")
print(dir())
print(divmod(5,4))
float('+1.23')
float('1e5')
float('1E-006')
float('  -12345\n')
print(globals())
for item in numList:
    print(hex(item))
print(len(numList))
print(len(floatList))
print(locals())
#print(map(even, numList)) #works in SML, and apparently my brain 
#is still in SML mode
print(max(numList))
print(max(floatList))
print(min(numList))
print(min(floatList))
for item in numList:
    print(oct(item))
#for item in floatList:
 #   print(oct(item))
#oct doesn't like float inputs :(
print(pow(5,4))
print(reversed(numList)) #oops






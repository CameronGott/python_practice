import string

def intro ():
    print("Hello there!")
    print("Today's code will be encapsulated into functions;")
    print("I'm tired of cluttered terminal output.")
class BoringObject:
    'Insert useful class documentation string here.'
    boringScoreCap = 11
    boringScore = 10

    def _init_(self):
        self.boringScoreCap = 11
        self.boringScore = 10
    def howBoring(self):
        return f'Boring score: {self.boringScore} out of {self.boringScoreCap}'

def practiceChunkOne():
    boringThing = BoringObject()
    #prints a memory address, cool!
    #But I'm in a VM, so I wonder how many times that
    #address has been abstracted away from the true
    #on-chip address
    print(repr(boringThing))
    numList = list(range(0,10))
    coolestSet = set(numList)
    print(coolestSet)
    #print(numList.slice(2,5)) that doesn't work
    print(sorted(numList, reverse=True))
    print(sum(numList))
    print(type(boringThing))
    print(vars(boringThing))

def practiceChunkTwo_stringBooGaLoo():
    print(string.ascii_lowercase)
    print(string.ascii_uppercase)
    letterList = ['a', 'b', 'e', 'g', 'e', 'p', '5', '@', '^']
    for letter in letterList:
        if (letter in string.ascii_lowercase):
            print(f"{letter} is in! woo!")
        else:
            print(f"{letter} isn't in! Booo")
    print(string.digits)
    print(string.hexdigits)


intro()
bor1 = BoringObject()
print(bor1.howBoring())
practiceChunkOne()
practiceChunkTwo_stringBooGaLoo()
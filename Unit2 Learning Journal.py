
#Learning Journal Unit 2

#Part 1

pi = 3.141592653589793  # I could have assigned this variable inside the func print_volume, however, the value of pi is a global constant and will be the same no matter where or why I call upon it in the future

def print_volume(r):

    volSphere = 4/3 * pi * r ** 3

    print('The volume of a sphere with radius ' + str(r) + ' is ' + str(volSphere) + '.')
    # I added this line of code to make the output easier to read. I ran into an issue where I could not concatonate str with int, so I got to utilize the str() function



print_volume(4)     # calling the function with 3 different values for r

print()     # I will use print() to put blank lines between our outputs for easier readability

print_volume(13)

print()

print_volume(5.5)

print()

print('This concludes part 1')

print()

# Part 2

import math # I could have imported this at the top of the script and used it to call pi for part 1 but I left it here so that I could note that I recognize this missed opportunity


def all4nothing(x,y):   # This function runs 2 arguments through a couple of equations that showcase a few elements that we learned this week

    m = math.sqrt((x / y) ** math.pi) / 2 #calling math module

    print((x + y * m) * 0)  #by the end of it all, anything multiplied by 0 is 0, hence the name of the function
    

all4nothing(4,9)

print()

all4nothing(math.pi,7.11)   #calling the math module as an argument

print()

all4nothing(len("I'm just playing around with some new tools I've picked up"),2)   #using embedded function as an argument

print()

print('This concludes part 2 and it was all for nothing')





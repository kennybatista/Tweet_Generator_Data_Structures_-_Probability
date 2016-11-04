#The sys module allows us to access the command line arguments.
import sys
# the random module allows us to use functions for randomly generating number or shuffling list elements.
import random

# this variable stores the command line arguments that the file is taking in.
arrayOfArgumentsPassedIn = sys.argv

def shuffle_in_place(arrayOfArgumentsPassedIn):
    # len returns the length of a sequence
    array_len = len(arrayOfArgumentsPassedIn)
    assert array_len > 2, 'Array is too short to shuffle!'
    # range() it tells us when it'll stop shuffling.
    for index in range(array_len):
        swap = random.randrange(array_len - 1)
        swap += swap >= index
        arrayOfArgumentsPassedIn[index], arrayOfArgumentsPassedIn[swap] = arrayOfArgumentsPassedIn[swap], arrayOfArgumentsPassedIn[index]


# array = list(range(5))
# shuffle(arrayOfArgumentsPassedIn)
arrayOfArgumentsPassedIn
shuffle_in_place(arrayOfArgumentsPassedIn)
print arrayOfArgumentsPassedIn

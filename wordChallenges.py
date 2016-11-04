#The sys module allows us to access the command line arguments.
import sys
# the random module allows us to use functions for randomly generating number or shuffling list elements.
import random

# this variable stores the command line arguments that the file is taking in.
arrayOfArgumentsPassedIn = sys.argv
# The shuffled variable stores the passed in arguments and randomly shuffles it by using the random module
# shuffled = random.shuffle(list_of_command_line_arguments)

def shuffle(arrayOfArgumentsPassedIn):
    copy = list(arrayOfArgumentsPassedIn)
    shuffle_in_place(copy)
    return copy

def shuffle_in_place(arrayOfArgumentsPassedIn):
    array_len = len(arrayOfArgumentsPassedIn)
    assert array_len > 2, 'Array is too short to shuffle!'
    for index in range(array_len):
        swap = random.randrange(array_len - 1)
        swap += swap >= index
        arrayOfArgumentsPassedIn[index], arrayOfArgumentsPassedIn[swap] = arrayOfArgumentsPassedIn[swap], arrayOfArgumentsPassedIn[index]


array = list(range(3))
shuffle(arrayOfArgumentsPassedIn)
arrayOfArgumentsPassedIn
shuffle_in_place(arrayOfArgumentsPassedIn)
print arrayOfArgumentsPassedIn

# This variable stores the command line arguments that the file takes in.
list_of_command_line_arguments = sys.argv
# The shuffled variable stores the passed in arguments and randomly shuffles them by using the random.shuffle method
shuffled = random.shuffle(list_of_command_line_arguments)

# Here we print the shuffled list
print(list_of_command_line_arguments)

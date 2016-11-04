#The sys module allows us to access the command line arguments.
import sys
# the random module allows us to use functions for randomly generating number or shuffling list elements.
import random

# This variable stores the command line arguments that the file takes in.
list_of_command_line_arguments = sys.argv
# The shuffled variable stores the passed in arguments and randomly shuffles them by using the random.shuffle method
shuffled = random.shuffle(list_of_command_line_arguments)

# Here we print the shuffled list
print(list_of_command_line_arguments)

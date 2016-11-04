#The sys module allows us to access the command line arguments
import sys
# the random module allows us to us functions for randomly or generating numbers or lists
import random

# this variable stores the command line arguments that the file is taking in.
list_of_command_line_arguments = sys.argv
# The shuffled variable stores the passed in arguments and randomly shuffles it by using the random module
shuffled = random.shuffle(list_of_command_line_arguments)

# Here wre print
print(list_of_command_line_arguments)

#The sys module allows us to access the command line arguments.
import sys
# The random module allows us to use functions for randomly generating integers or shuffling a list of elements.
import random

# CHALLENGE!: Build a script that reaaranges words in a lists.

# PSEUDOCODE:
# sampleData = ['kenny','is','the','awesomest','guy']
# reaarangedList = []
# loop through the 'sampleData' list
# create random integer, which we'll use as a random index for the word
# Attach the new random index to the words and add to the 'reaarangedList'
# if there is an element that I don'w want, remove it
# print the new rearranged list

# Here we store our list of arguments.
sample_Data = sys.argv
# List where we will store our newly arranged words.
rearranged_words = []

# Here we loop through the system argument list
for word in range(1, len(sample_Data)):
    # we have the -1 at the end of this statement so that we don't get an index out of range error.
    # Since we begin at one, then do len(sample_Data) which is the amount we type in the command line, let's say 2. It's like saying that we begin at one, then end in 3 more indexes, but since we began at one we skipped the 0, so with the -1 we bring it back so it won't crash.
    random_Int = random.randint(1, len(sample_Data)-1)
    rearranged_words.append(sample_Data[random_Int])
    sample_Data.remove(sample_Data[random_Int])


print(rearranged_words)

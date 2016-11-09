import sys

# PSEUDOCODE
# create the method


# 1. Create method signature
# 2. Open up the file
# 3. Read the file and store data in variable
# 4. Split the words in the file and store in an array.
# 5. Print the splitted words

#1
def readFromFileAndOutputAListOfWords():
    #2 - open is an object which we store in f
    f = open('/Users/kennybatista/Desktop/words.txt','r')
    #3 - we read from the f object
    words = f.read()
    #4 - After reading the file and storing the data in a words container
    # we split each word and store it inside of a collection data type called listOfSplittedWords
    listOfSplittedWords = words.split()

    sentence = ""
    for i in listOfSplittedWords:
        # sentence += " "
        sentence += " " + i
    print sentence

# make sure that the method runs and outputs info
readFromFileAndOutputAListOfWords()

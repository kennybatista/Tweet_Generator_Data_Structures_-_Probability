import random

def corpus():
        file_to_open = open("./words.txt","r")
        file_to_read = file_to_open.read()
        file_to_split = file_to_read.split()
        list_of_words = file_to_split
        return list_of_words

def histogram(list_of_words): # MARK: Task #1
    word_dict = {} # Empty Dictionary

    for word in list_of_words:     # loop through all of the words ----------- # if the current looping word is an existing key, access the statement
        if word in word_dict.keys():
            word_dict[word] += 1 # if the statement was accessed it means that the key was found, and that the key's (word_count[word]) value will be have += 1 added to it
        else: # if the current word being looped is not a key, then add the current word as a loop and set 1 as it's value
            word_dict[word] = 1

    unique_words = len(word_dict) # print the dictionary => { 'and': 89, 'run': 23 }
    return word_dict

def unique_words(unique_words): # MARK: Task #2
    print ' There are ' + str(len(unique_words)) + ' unique words ' + 'in the dictionary'

def frequency(word_passed_in_is, histogram): # it will take in a word, and a list
        if word_passed_in_is in histogram.keys(): # If that word we passed in is in the histogram(either key or value in the dictionary)
            print 'The word "' + word_passed_in_is + '" is frequent ' + str(histogram[word_passed_in_is]) + ' times' # prints the value of the key
        else:
            print "that word does not exits in the corpus"

def stochastic_random(list_of_words):
    # random_int = random.randint(0, len(list_of_words)-1)
    print 'Here is a random word: ' + random.choice(list_of_words.keys())
    # return l

# we assign the returned single evaluated value to the text container
text = corpus()
# We pass in the "corpus's " returned value, which is a "list of dictionary"
histogram(text)
histogram = histogram(text)
unique_words(histogram)
frequency("and", histogram)
stochastic_random(histogram)

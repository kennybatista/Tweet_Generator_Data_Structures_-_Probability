from pprint import pprint
# This method will return the corpus
def corpus():
        # opens the file in read mode
        file_to_open = open("./words.txt","r")
        # reads the file
        file_to_read = file_to_open.read()
        # splits all of the words into a new list
        file_to_split = file_to_read.split()
        # we place the list of values in a container
        list_of_words = file_to_split
        # we return it for whoever calls this method
        return list_of_words

# This method takes in a corpus, and returns a histogram from it
def histogram(list_of_words): # MARK: Task #1
    # Empty Dictionary
    histogram = {}

    # loop through all of the words ----------- # if the current looping word is an existing key, access the statement
    for word in list_of_words:
        if word in histogram.keys():
            histogram[word] += 1 # if the statement was accessed it means that the key was found, and that the key's (word_count[word]) value will be have += 1 added to it
        else: # if the current word being looped is not a key, then add the current word as a loop and set 1 as it's value
            histogram[word] = 1

    # print our histogram data structure
    # pprint(histogram)
    return histogram

# MARK: Task #2
def unique_words(histogram):
    print '- There are ' + str(len(histogram)) + ' unique words in the corpus'


def frequency(word_passed_in_is, histogram): # it will take in a word, and a list
        if word_passed_in_is in histogram.keys(): # If that word we passed in is in the histogram(either key or value in the dictionary)
            print '- The word: and, shows up ' + str(histogram[word_passed_in_is]) + ' times' # prints the value of the key
        else:
            print "that word does not exits in the corpus"

text = corpus()
histogram(text)
histogram = histogram(text)
unique_words(histogram)
frequency("and", histogram)

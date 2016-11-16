def corpus():
        file_to_open = open("./words.txt","r")
        file_to_read = file_to_open.read()
        file_to_split = file_to_read.split()
        list_of_words = file_to_split
        return list_of_words

def histogram(list_of_words): # MARK: Task #1
    word_count = {} # Empty Dictionary

    for word in list_of_words:     # loop through all of the words ----------- # if the current looping word is an existing key, access the statement
        if word in word_count.keys():
            word_count[word] += 1 # if the statement was accessed it means that the key was found, and that the key's (word_count[word]) value will be have += 1 added to it
        else: # if the current word being looped is not a key, then add the current word as a loop and set 1 as it's value
            word_count[word] = 1

    unique_words = len(word_count) # print the dictionary => { 'and': 89, 'run': 23 }
    return word_count

def unique_words(unique_words): # MARK: Task #2
    print len(unique_words)

def frequency(word_passed_in_is, histogram): # it will take in a word, and a list
        if word_passed_in_is in histogram.keys(): # If that word we passed in is in the histogram(either key or value in the dictionary)
            print histogram[word_passed_in_is] # prints the value of the key
        else:
            print "that word does not exits in the corpus"

text = corpus()
histogram(text)
histogram = histogram(text)
unique_words(histogram)
frequency("and", histogram)

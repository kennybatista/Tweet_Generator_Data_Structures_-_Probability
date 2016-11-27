import random
import os
from flask import Flask


app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, Kenny!'




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
    print '- There are ' + str(len(histogram)) + ' unique words in the corpus'
    return '- There are ' + str(len(histogram)) + ' unique words in the corpus'

def frequency(word_passed_in_is, histogram): # it will take in a word, and a list
        if word_passed_in_is in histogram.keys(): # If that word we passed in is in the histogram(either key or value in the dictionary)
            print '- The word "' + word_passed_in_is + '" is frequent ' + str(histogram[word_passed_in_is]) + ' times' # prints the value of the key
            print ""
        else:
            print "that word does not exits in the corpus"




def stochastic_random(histogram_dict):

    # one random word
    # print '- ' + random.choice(histogram_dict.keys()) + ' -> ' + str(random.choice(histogram_dict.values()))

    random_sentence_list = []
    random_sentence = ""

    for i in range(0, 10):
        random_sentence_list.append(random.choice(histogram_dict.keys()))

    for word in random_sentence_list:
        random_sentence += word + ' '

    print random_sentence
    return random_sentence

@app.route('/')
def print_to_flask():
    return stochastic_random(histogram)
# we assign the returned single evaluated value to the text container
text = corpus()
# We pass in the "corpus's " returned value, which is a "list of dictionary"
histogram(text)
# We store the created histogram inside of a variable called histogram
histogram = histogram(text)
# we pass in the histogram to the unique words method, which then prints out the count of items in the dictionary
unique_words(histogram)
# to to freqency method, we pass in a word, and a histogram, then it will return the count of times that the word shows up in the histogram dictionary
frequency("and", histogram)
# we return a random word
# stochastic_random(histogram)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

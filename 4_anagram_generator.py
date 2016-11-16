import sys, random


# THIS ANAGRAM GENERATOR IS NOT WORKING YET

# method signature
def generate_anagram():
    # the list method will break a word apart and add each letter to a list data structure

    list_of_letters_from_word_input = list(sys.argv[1])
    # we store the count of the elements in the list above
    length_of_word_list = len(list_of_letters_from_word_input)

    possible_indexes = length_of_word_list - 1


    new_anagram = []
    for letter in range(-1, length_of_word_list):
        random_integer = random.randint(0, possible_indexes)

        list_of_letters_from_word_input[letter], list_of_letters_from_word_input[random_integer] = list_of_letters_from_word_input[random_integer],list_of_letters_from_word_input[letter]

        new_anagram.append(list_of_letters_from_word_input[random_integer])


        # new_anagram.append(list_of_letters_from_word_input[random_integer])
    concatenate_indexes = "".join(list_of_letters_from_word_input)
    newer_anagram = "".join(new_anagram)

    print concatenate_indexes, newer_anagram









# create method
# convert the letters in the input variable into a list
# loop over the list
# create a random integer from 0 to #oflettersInword
# assign that randomInt to an index in the list holding the letters for the word_file
# return the new word

generate_anagram()

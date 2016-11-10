import sys, random


# PSEUDOCODE:
# 1. Create method signature
# 2. Open up the file
# 3. Read the file and store data in variable
# 4. Split the words in the file and store in an array.
# 5. Print the splitted words for testing
# 6.

def read_from_file_and_output_a_list_of_words():
        # use the open() object to open the file, use 'r' for read mode.
        # If I wanted to write to the file I would use 'w'
        word_file = open('./words.txt','r')
        # Read the file and store all the data ( separated in new lines ) in a variable
        words_stored_in_list_data_structure = word_file.read()
        # Split each new lined word and store it in a list data structures
        list_of_splitted_words_stored_in_a_list = words_stored_in_list_data_structure.split()
        # Before I added the int(), this was a list, and if i tried looping through sys.argv[1] it would just give me the amount of elements on the list. So that's why I joited them from 1,0,0 to 100 and turned it into an integer
        valueOfArgumentPassed = int(''.join(sys.argv[1]))

        sentence = []

        if valueOfArgumentPassed > len(list_of_splitted_words_stored_in_a_list):
            print 'ERROR!!!PANIC: You have submitted a value as an argument that is greater than the amount of words in the corpus'
        else:
            for i in range(0, valueOfArgumentPassed):
                random_Integer = random.randint(0, len(list_of_splitted_words_stored_in_a_list))
                sentence.append(list_of_splitted_words_stored_in_a_list[random_Integer])

        new_sentence = ' '.join(sentence)
        print new_sentence

# read_from_file_and_output_a_list_of_words()


read_from_file_and_output_a_list_of_words()

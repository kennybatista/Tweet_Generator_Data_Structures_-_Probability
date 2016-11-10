import sys, random
# PSEUDOCODE:
# 1. Create method signature
# 2. Open up the file
# 3. Read the file and store data in variable
# 4. Split the words in the file and store in an array.
# 5. Print the splitted words for testing
# 6.

def read_from_file_and_output_a_list_of_words():
        f = open('/Users/kennybatista/Desktop/words.txt','r')
        words = f.read()
        # all of the words in the txt file transferred to a list
        listOfSplittedWords = words.split()
        # before I added the int(), this was a list, and if i tried looping through sys.argv[1] it would just give me the amount of elements on the list. So that's why I joited them from 1,0,0 to 100 and turned it into an integer
        valueOfArgumentPassed = int(''.join(sys.argv[1]))

        sentence = []

        if valueOfArgumentPassed > len(listOfSplittedWords):
            print 'ERROR!!!PANIC: You have submitted a value as an argument that is greater than the amount of words in the corpus'
        else:
            for i in range(0, valueOfArgumentPassed):
                random_Integer = random.randint(0, len(listOfSplittedWords))
                sentence.append(listOfSplittedWords[random_Integer])

        new_sentence = ' '.join(sentence)
        print new_sentence

read_from_file_and_output_a_list_of_words()

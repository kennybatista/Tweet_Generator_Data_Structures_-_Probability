import sys

# CHALLENGE!: String reversals: reverse words, sentences

# PSEUDOCODE:
# Create a (1)single word variable or a (2)list containing words
# Loop through every character of the word. Loop thorugh every character on the loops index word
# During every iteration grab the last letter and add it to a new variable that will hold the newly arranged word.

sub_reversed_word = "love"
post_reversed_word = ""



# for character in range(0,len(sub_reversed_word)):
#     post_reversed_word = sub_reversed_word[len(sub_reversed_word) -1 -i] +
#
# print post_reversed_word

def reverse_word(word):
    reverse_word = ""
    for i in range(0, len(word)):
        reverse_word += word[len(word) - 1 - i] + " "
        return reverse_word

print reverse_word(word[0])

#
# def reverse_word(word):
#     '''This function
#     :return the orignal word reversed
#     '''
#     reversed_word = ""
#     for i in range(0, len(word)):
#         reversed_word += word[len(word) - 1 - i]
#     return reversed_word

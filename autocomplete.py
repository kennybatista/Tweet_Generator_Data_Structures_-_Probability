import enchant

beginningOfWord = raw_input("For an autocomplete, type in the first letter of a word: ")
englishDict = enchant.Dict("en_US")
print englishDict.suggest(beginningOfWord)

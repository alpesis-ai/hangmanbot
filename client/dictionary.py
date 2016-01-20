import re

import settings

def split_dict(dictpath=settings.DICT_PATH):

    words = {}

    dictfile = open(dictpath, 'r')
    for line in dictfile.readlines():
        thisLine = line.strip()
        wordLength = len(thisLine)
        if wordLength > 0:
            if wordLength not in words.keys():
                words[wordLength] = [thisLine]
            else:
                words[wordLength].append(thisLine)

    return words

def count_frequency(words):
    """
    >>> count_frequnecy(wordDict[10])
    """

    letterFreq = {}

    for word in words:
        for letter in word:
            if letter not in letterFreq.keys():
                letterFreq[letter] = 1
            else:
                letterFreq[letter] += 1

    letterFreq = sorted(letterFreq.items(), key=lambda x: x[1], reverse=True)
    return letterFreq

def search_pattern(wordDict, guessWord, pattern):

    matches = []

    wordLength = len(guessWord)
    for word in wordDict[wordLength]:
        match = re.search(str(pattern), word)
        matches.append(match.group()) if match else matches

    return matches

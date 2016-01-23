"""
Processing the external dictionaries.
"""


def split_dict(dictpath):
    """Returns a wordDict(wordLength, words) from a dictionary.

    example:
             words = {
                       1: ['word1', 'word2', ...],
                       2: ['word1', 'word2', ...]
                       ...
                      }
    """

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


def split_dicts(dictpaths):
    """Returns a wordDict(wordLength, words) from some dictionaries.

    example:
             words = {
                       1: ['word1', 'word2', ...],
                       2: ['word1', 'word2', ...]
                       ...
                      }
    """

    words = {}

    for dictpath in dictpaths:
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

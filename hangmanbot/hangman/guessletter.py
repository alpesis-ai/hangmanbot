"""
-------------------------------------
How to select a letter (strategies)
-------------------------------------

    get_letter()
        |
        |---> count_unknown()
        |
        |---> _search_vowels()
        |---> _search_pattern()
                  |
                  |---> _create_word_pattern()
                  |---> _search_word_pattern()
                  |
                  |---> _create_letter_pattern() --> _find_ngram()
                  |---> _match_letter_pattern()
                  |---> _select_letter()

"""


import re
import logging

import settings

LOG = logging.getLogger('guessletter')


def get_letter(givenWord, guessedLetters):
    """Returns a letter by searching vowels and patterns.
    """

    wordLength = len(givenWord)
    numOfUnknown = count_unknown(givenWord)

    if numOfUnknown == wordLength:
        LOG.debug("* searching a vowel...")
        letter = _search_vowels(wordLength, guessedLetters)
    elif numOfUnknown < wordLength:
        LOG.debug("* searching a pattern...")
        letter = _search_pattern(givenWord, wordLength, guessedLetters)
    else:
        raise "Error"

    return letter


def count_unknown(givenWord):
    """Returns # of unknown letters of a given word.
    """
    return sum([1 for letter in givenWord if letter == '*'])

#-----------------------------------------------------------------------------#


def _search_vowels(wordLength, guessedLetters):
    """Returns an unguessed vowel cross checking against the vowel dict.
    """

    vowelDict = settings.OPTIMIZED_DICT_BOOK[wordLength]
    matchedLetters = [letter for letter in vowelDict if letter not in guessedLetters]
    return matchedLetters[0]


def _search_pattern(givenWord, wordLength, guessedLetters):
    """Returns an unguessed letter by searching the letter patterns.
    """

    wordPattern = _create_word_pattern(givenWord, guessedLetters)
    matchedWords = _search_word_pattern(settings.WORDDICT, wordLength, wordPattern)

    numOfMatchedWords = len(matchedWords)
    if numOfMatchedWords == 0:
        LOG.debug("matchWords(0): searching ngrams/patterns by a dictionary")
        letterPatterns = _create_letter_pattern(givenWord, guessedLetters)
        matchedLetters = _match_letter_pattern(settings.WORDDICT[wordLength], letterPatterns)
        letter = _select_letter(matchedLetters, guessedLetters)
        return letter

    elif numOfMatchedWords == 1:
        LOG.debug("matchWords(1): return this word")
        thisWord = matchedWords[0]
        matchedLetters = [letter for letter in thisWord if letter not in guessedLetters]
        return matchedLetters[0]

    elif numOfMatchedWords > 1:
        LOG.debug("matchWords(>1): searching ngrams/patterns in matchWords")
        letterPatterns = _create_letter_pattern(givenWord, guessedLetters)
        matchedLetters = _match_letter_pattern(matchedWords, letterPatterns)
        letter = _select_letter(matchedLetters, guessedLetters)
        return letter

    else:
        raise "SearchPatternError"

#-----------------------------------------------------------------------------#


def _create_word_pattern(givenWord, guessedLetters):
    """Returns the word pattern.
    """

    # subPattern: [^iac]
    letters = [letter.lower() for letter in guessedLetters]
    subPattern = '[^' + ''.join(letter for letter in letters) + ']'

    # pattern: [^iac][^iac]ia[^iac]
    pattern = [subPattern if letter == '*' else letter.lower() for letter in givenWord]
    pattern = ''.join(letter for letter in pattern)
    LOG.debug("pattern: %s " % pattern)

    return pattern


def _search_word_pattern(wordDict, wordLength, pattern):
    """Returns matchedWords by the word pattern.
    """

    matchedWords = []

    if wordLength in wordDict.keys():
        for word in wordDict[wordLength]:
            matchedWord = re.search(str(pattern), word)
            if matchedWord:
                matchedWords.append(matchedWord.group())

    return matchedWords


def _create_letter_pattern(givenWord, guessedLetters):
    """Returns letter patterns by finding ngram.
    """

    # subPattern: [^dc]
    letters = [letter.lower() for letter in guessedLetters]
    subPattern = '([^' + ''.join(letter for letter in letters) + '])'

    # letterGrams: i.e. [*ab], [ab*]
    # letterPatterns: one unknown letter allowed, i.e. ab[^dc], [^dc]ab
    matchedPatterns = []
    numOfKnown = len(givenWord) - count_unknown(givenWord)
    for thisNumOfKnown in range(1, numOfKnown+1):
        letterGrams = _find_ngram([letter for letter in givenWord.lower()],
                                  thisNumOfKnown+1)

        for letterGram in letterGrams:
            thisNumOfUnknown = count_unknown(letterGram)
            if thisNumOfUnknown == 1:
                thisPattern = [subPattern if letter == '*' else letter.lower() for letter in letterGram]
                thisPattern = ''.join(letter for letter in thisPattern)
                matchedPatterns.append(thisPattern)

    return matchedPatterns


def _match_letter_pattern(matchedWords, letterPatterns):
    """Returns matchedLetters by the letter patterns.
    """

    LOG.debug("matchedWords: %s" % matchedWords)
    LOG.debug("letterPatterns: %s" % letterPatterns)

    matchedLetters = []
    for letterPattern in letterPatterns:
        letterPattern = ".*" + letterPattern + ".*"
        LOG.debug("letterPattern: %s" % letterPattern)
        for matchedWord in matchedWords:
            # print "matchedWord: %s" % matchedWord
            thisMatchedLetter = re.match(letterPattern, matchedWord)
            # print "thisMatchedLetter: %s" % thisMatchedLetter
            if thisMatchedLetter is not None:
                matchedLetters.append(thisMatchedLetter.group(1))

    LOG.debug("matchedLetters: %s" % matchedLetters)
    return matchedLetters


def _select_letter(matchedLetters, guessedLetters):
    """Returns a letter by frequnecy count.
    """

    letterFreq = {}

    for matchedLetter in matchedLetters:
        if matchedLetter not in letterFreq.keys():
            letterFreq[matchedLetter] = 1
        else:
            letterFreq[matchedLetter] += 1
    letterFreq = sorted(letterFreq.items(), key=lambda x: x[1], reverse=True)

    letters = []
    for letter, freq in letterFreq:
        if letter not in guessedLetters:
            letters.append(letter)

    return letters[0]


def _find_ngram(words, n):
    """Returns letter ngram by n in a word.
    """

    return zip(*[words[i:] for i in range(n)])

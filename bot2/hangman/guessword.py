import re

import settings

def get_letter(givenWord, guessedLetters):

    wordLength = len(givenWord)
    numOfUnknown = count_unknown(givenWord)    

    if numOfUnknown == wordLength:
        print "* searching a vowel..."
        letter = _search_vowels(givenWord, wordLength, guessedLetters)
    elif numOfUnknown < wordLength:
        print "* searching a pattern..."
        letter = _search_pattern(givenWord, wordLength, numOfUnknown, guessedLetters)
    else:
        raise "Error" 

    return letter 

def count_unknown(givenWord):
    return sum([1 for letter in givenWord if letter == '*'])

#-----------------------------------------------------------------------------#

def _search_vowels(givenWord, wordLength, guessedLetters):
  
    matchedLetters = [letter for letter in settings.OPTIMIZED_DICT_BOOK[wordLength] if letter not in guessedLetters]
    return matchedLetters[0]

def _search_pattern(givenWord, wordLength, numOfUnknown, guessedLetters):

    wordPattern = _create_word_pattern(givenWord, guessedLetters)
    matchedWords = _search_word_pattern(settings.WORDDICT, wordLength, wordPattern)

    numOfMatchedWords = len(matchedWords)
    if numOfMatchedWords == 0:
        print "matchWords(0): searching ngrams/patterns by a dictionary"
        letterPatterns = _create_letter_pattern(givenWord, guessedLetters)
        matchedLetters = _match_letter_pattern(settings.WORDDICT[wordLength], letterPatterns)
        letter = _select_letter(matchedLetters, guessedLetters)
        return letter

    elif numOfMatchedWords == 1:
        print "matchWords(1): return this word"
        thisWord = matchedWords[0]
        matchedLetters = [letter for letter in thisWord if letter not in guessedLetters]
        return matchedLetters[0]

    elif numOfMatchedWords > 1:
        print "matchWords(>1): searching ngrams/patterns in matchWords"
        letterPatterns = _create_letter_pattern(givenWord, guessedLetters)
        matchedLetters = _match_letter_pattern(matchedWords, letterPatterns)
        letter = _select_letter(matchedLetters, guessedLetters)
        return letter

    else:
        raise "SearchPatternError"

#-----------------------------------------------------------------------------#

def _create_word_pattern(givenWord, guessedLetters):
    
    # subPattern: [^iac]
    letters = [letter.lower() for letter in guessedLetters]
    subPattern = '[^' + ''.join(letter for letter in letters) + ']'
  
    # pattern: [^iac][^iac]ia[^iac]
    pattern = [subPattern if letter == '*' else letter.lower() for letter in givenWord]
    pattern = ''.join(letter for letter in pattern)
    print "pattern: %s " % pattern

    return pattern

def _search_word_pattern(wordDict, wordLength, pattern):

    matchedWords = []
    
    if wordLength in wordDict.keys():
        for word in wordDict[wordLength]:
            matchedWord = re.search(str(pattern), word)
            matchedWords.append(matchedWord.group()) if matchedWord else matchedWords

    return matchedWords

def _create_letter_pattern(givenWord, guessedLetters):

    # subPattern: [^dc]
    letters = [letter.lower() for letter in guessedLetters]
    subPattern = '([^' + ''.join(letter for letter in letters) + '])'

    # letterGrams: i.e. [*ab], [ab*]
    # letterPatterns: one unknown letter allowed, i.e. ab[^dc], [^dc]ab
    matchedPatterns = []
    numOfKnown = len(givenWord) - count_unknown(givenWord)
    for thisNumOfKnown in range(1, numOfKnown+1):
        letterGrams = _find_ngram([letter for letter in givenWord.lower()], thisNumOfKnown+1)
        
        for letterGram in letterGrams:
            thisNumOfUnknown = count_unknown(letterGram)
            if thisNumOfUnknown == 1:
                thisPattern = [subPattern if letter == '*' else letter.lower() for letter in letterGram]
                thisPattern = ''.join(letter for letter in thisPattern)
                matchedPatterns.append(thisPattern)

    return matchedPatterns

def _match_letter_pattern(matchedWords, letterPatterns):

    print "matchedWords: %s" % matchedWords
    print "letterPatterns: %s" % letterPatterns

    matchedLetters = []
    for letterPattern in letterPatterns:
        letterPattern = ".*" + letterPattern + ".*"
        print "letterPattern: %s" % letterPattern
        for matchedWord in matchedWords:
            # print "matchedWord: %s" % matchedWord
            thisMatchedLetter = re.match(letterPattern, matchedWord)
            # print "thisMatchedLetter: %s" % thisMatchedLetter
            if thisMatchedLetter is not None:
                # print "thisMatchedLetter.group: %s" % thisMatchedLetter.group(1) 
                matchedLetters.append(thisMatchedLetter.group(1))
   
    print "matchedLetters: %s" % matchedLetters 
    return matchedLetters

def _select_letter(matchedLetters, guessedLetters):

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
    return zip(*[words[i:] for i in range(n)])

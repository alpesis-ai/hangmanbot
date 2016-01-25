"""
Collecting the guessedWords.
"""

import os.path

import settings.settings as settings


def collect_words(guessedWord):
    """Saving the guessedWord by correctGuesses and incorrectGuesses.
    """

    if '*' in guessedWord:
        _process_words(guessedWord, settings.INCORRECT_GUESSES_FILEPATH)
    else:
        _process_words(guessedWord, settings.CORRECT_GUESSES_FILEPATH)


def _process_words(guessedWord, filepath):
    """Saving the words in a file.
    """

    if os.path.exists(filepath):
        words = _read_words(filepath)
        if guessedWord.lower() not in words:
            thisWord = "%s\n" % guessedWord.lower()
            _save_words(filepath, thisWord)
    else:
        thisWord = "%s\n" % guessedWord.lower()
        _save_words(filepath, thisWord)


def _read_words(inpath):
    """Reading the words from a file.
    """

    words = []
    with open(inpath, 'r') as wordFile:
        for line in wordFile.readlines():
            words.append(line.strip())

    return words


def _save_words(outpath, word):
    """Saving a word in a file.
    """

    open(outpath, 'a+').write(word.lower())

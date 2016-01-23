import os.path

import settings

def collect_words(guessedWord):

    if '*' in guessedWord:
        _process_words(guessedWord, settings.INCORRECT_GUESSES_FILEPATH)
    else:
        _process_words(guessedWord, settings.CORRECT_GUESSES_FILEPATH)

def _process_words(guessedWord, filepath):

    if os.path.exists(filepath):
        words = _read_words(filepath)
        if guessedWord.lower() not in words:
            thisWord = "%s\n" % guessedWord.lower()
            _save_words(filepath, thisWord)
    else:
        thisWord = "%s\n" % guessedWord.lower()
        _save_words(filepath, thisWord)

def _read_words(inpath):
    words = []
    with open(inpath, 'r') as f:
        for line in f.readlines():
            words.append(line.strip())

    return words

def _save_words(outpath, word):
    open(outpath, 'a+').write(word.lower())

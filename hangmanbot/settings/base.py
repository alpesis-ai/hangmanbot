"""Configuration of hangmanbot."""

import os.path

import dicts.worddict

#-------------------------------------------------------------------#
# ROOT SETTINGS

# root path
CURRENT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROJECT_ROOT = os.path.dirname(CURRENT_DIR)

#-------------------------------------------------------------------#
# ACCOUNT SETTINGS

# request url and play id
REQUEST_URL = "Your_Request_URL"
PLAYER_ID = "Your_Player_ID"


#------------------------------------------------------------------#
# DICTIONARY SETTINGS

# the below dictionaries are used for searching the patterns of
# the unknown given words
#
# - step 1
#   - (optimized_word_dict) search a vowel for a unknown given word
# - step 2
#   - (correct_guesses, incorrect_guesses) search the pattern of a given word
#   - (dict, extra_dict) search the pattern of a given word
# - step 3 (pending)
#   - (word root, suffixes, prefixes) search the subpattern of a given word


# external dictionary
# http://www-01.sil.org/linguistics/wordlists/english/
DICT_PATH = PROJECT_ROOT + "/files/dicts/wordsEn.txt"
# extra words (added by the users)
EXTRA_DICT_PATH = PROJECT_ROOT + "/files/dicts/extra_words.txt"

# wordDict generated from the external dictionary and custom words
if os.path.exists(EXTRA_DICT_PATH):
    WORDDICT = dicts.worddict.split_dicts([DICT_PATH, EXTRA_DICT_PATH])
else:
    WORDDICT = dicts.worddict.split_dict(DICT_PATH)

# words generated from HangmanServer (automatical generation)
# saving the correct and incorrect guessed words
CORRECT_GUESSES_FILEPATH = PROJECT_ROOT + '/files/dicts/correct_guesses.txt'
INCORRECT_GUESSES_FILEPATH = PROJECT_ROOT + '/files/dicts/incorrect_guesses.txt'

# alphabet
# ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
#             'h', 'i', 'j', 'k', 'l', 'm', 'n',
#             'o', 'p', 'q', 'r', 's', 't', 'u',
#             'v', 'w', 'x', 'y', 'z']
# calculating the frequencies from a dictionary
ALPHABET = ['e', 's', 'i', 'a', 'r', 'n', 't',
            'o', 'l', 'c', 'b', 'u', 'g', 'p',
            'm', 'h', 'b', 'y', 'f', 'v', 'k',
            'w', 'z', 'x', 'j', 'q']

# optimized_dict_book by vowels
# calculating the frequencies from a dictionary
OPTIMIZED_DICT_BOOK = {
    1: ['a', 'i'],
    2: ['a', 'o', 'e', 'i', 'u'],
    3: ['a', 'e', 'o', 'i', 'u'],
    4: ['e', 'a', 'o', 'i', 'u'],
    5: ['e', 'a', 'o', 'i', 'u', 'y'],
    6: ['e', 'a', 'i', 'o', 'u'],
    7: ['e', 'i', 'a', 'o', 'u'],
    8: ['e', 'i', 'a', 'o', 'u'],
    9: ['e', 'i', 'a', 'o', 'u'],
    10: ['e', 'i', 'a', 'o', 'u'],
    11: ['e', 'i', 'a', 'o', 'u'],
    12: ['e', 'i', 'a', 'o', 'u'],
    13: ['i', 'e', 'a', 'o'],
    14: ['i', 'e', 'a', 'o'],
    15: ['i', 'e', 'o', 'a'],
    16: ['i', 'e', 'o', 'a'],
    17: ['i', 'e', 'o', 'a'],
    18: ['i', 'e', 'o', 'a'],
    19: ['i', 'e', 'a'],
    20: ['i', 'a', 'e']
}

#-------------------------------------------------------------------#
# SCORE SETTINGS

# best score
BEST_SCORE_PATH = PROJECT_ROOT + "/files/score/best_score.txt"

#-------------------------------------------------------------------#
# LOGGING

LOGGING_CONF_PATH = PROJECT_ROOT + "/hangmanbot/conf/logging.conf"

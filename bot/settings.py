import os.path

import dicts.worddict

#-------------------------------------------------------------------#
# Path Settings

# root path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#------------------------------------------------------------------#
# Account Settings

# start game settings
REQUEST_URL = "https://strikingly-hangman.herokuapp.com/game/on"
PLAYER_ID = "kwailamchan@hotmail.com"

#------------------------------------------------------------------#
# guess

# word dicts
DICT_PATH = PROJECT_ROOT + "/dicts/wordsEn.txt"
EXTRA_DICT_PATH = PROJECT_ROOT + "/dicts/extra_words.txt"

if os.path.exists(EXTRA_DICT_PATH):
    WORDDICT = dicts.worddict.split_dicts([DICT_PATH, EXTRA_DICT_PATH])
else:    
    WORDDICT = dicts.worddict.split_dict(DICT_PATH)

# logging: guessed words
CORRECT_GUESSES_FILEPATH = PROJECT_ROOT + '/dicts/correct_guesses.txt'
INCORRECT_GUESSES_FILEPATH = PROJECT_ROOT + '/dicts/incorrect_guesses.txt'

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
# score

BEST_SCORE_PATH = PROJECT_ROOT + "/bot2/files/score/best_score.txt"

#-------------------------------------------------------------------#
# logging

SUBMIT_LOG_PATH = PROJECT_ROOT + "/bot2/files/logs/submit_logs.txt"

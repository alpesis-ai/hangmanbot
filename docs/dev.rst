#####################################
Development
#####################################

******************
Toolkits
******************

-------------------
Developement Flow
-------------------

::

    Setup --> Dev --> Test --> QA --> Devops --> Docs

-------------------
Devevlop Toolkits
-------------------

========= ===========================
 Flow      Tools                    
========= ===========================
 Dev      python, request, logging  
 Test     unittest, nose, ipython   
 QA       pep8, pylint              
 Docs     sphinx, sphinx-autobuild  
 DevOps   Makefile                  
========= ===========================


******************
Folder Structure
******************

main folders

::

    hangmanclient/
        \
        \---- hangmanbot/          # source code
        \---- files/               # dictionaries and score
        \---- requirements/        # python dependencies
        \
        \---- vagrant/             # Vagrantfile
        \---- docs/                # sphinx
        \
        \---- ...

hangmanbot

::

    hangmanbot/
        \---- settings.py                         # bot settings
        \---- run.py                              # run bot
        \
        \---- hangman/                         
        \        \---- hangmanserver.py           # hangmanServer API
        \        \---- (*) hangmanbot.py          # hangman bot
        \        \---- (*) guessletter.py         # letter selection
        \        \---- result.py                  # result processing
        \
        \---- dicts/ 
        \        \---- worddict.py                # dictionary processing
        \        \---- wordcollector.py           # guessedWords processing
        \---- conf/logging.conf                   # logging configurations


*****************
Source Code
*****************

-----------------
hangmanbot.py
-----------------

::

      start_game()
          |
          |---> SESSION
          |---> process_session()
          |          |---- WORD
          |          |---> _guess_word()
          |                     |---> letter=hangman.guessletter.get_letter()
          |                     |---> GUESS
          |                     |---> _get_result()
          |                               |---> RESULT
          |
          |---> process_result()
                     |---> _update_best_score()
                     |          |---> _get_result()
                     |                    |---> RESULT
                     |---> _submit_score()
                                |---> SUBMIT

-----------------
guessletter.py
-----------------

::

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


----------------
logging
----------------

logging.conf

- logger
- handler
  - consoleHandler
  - fileHandler
- formatter

Logging Rules

- debug
- info
- warning
- error

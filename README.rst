###########################################
Hangman Bot
###########################################

-----------------------
Introduction
-----------------------

HangmanBot is an app for automatically playing a Hangman Game.

So far, the performance of this bot is scored 1200+. Here was an score played by this bot:

::

    {
      "message": "GAME OVER",
      "sessionId": "2ad8f8430e3681c4dea8696ae19fb323",
      "data": {
        "playerId": "user@example.com",
        "sessionId": "2ad8f8430e3681c4dea8696ae19fb323",
        "totalWordCount": 80,
        "correctWordCount": 78,
        "totalWrongGuessCount": 231,
        "score": 1329,
        "datetime": "2016-01-22 14:26:57"
      }
    }

-----------------------
Get Started
-----------------------

Prequisitions

- Vagrant
- VirtualBox
- Ubuntu 14.04
- Python 2.7.x

Setup

::

    $ # cd to the project folder
    $ # copy Vagrantfile to a specfic path
    $ vagrant up

    $ vagrant ssh
    $ sudo apt-get update && upgrade
    $ sudo adduser hangman
    $ sudo chown -R hangman:hangman /hangman
    $ cd /hangman/hangman_client

    $ sudo apt-get install python-virtualenv
    $ sudo su hangman
    $ mkdir venvs
    $ virtualenv venvs/hangman_client
    $ source venvs/hangman_client/bin/activate
    $ cd hangman_client
    $ pip install -r requirements/base.txt
    $ pip install -r requirements/docs.txt
    $ pip install -r requirements/test.txt

    $ cd /path/to/hangmanbot
    $ python -m run

If you would like to read the fully detailed documents, please open the docs server.

::

    $ cd docs/
    $ sphinx-autobuild ./ ./_build/html -H 0.0.0.0

Then open ``http://localhost:8000`` on a browser.

-----------------------
Algorithms
-----------------------

Game Flow (``./hangmanbot/hangman/hangmanbot.py``)

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


Letter Selection (``./hangmanbot/hangman/guessletter.py``)

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


----------------------
Folder Structure
----------------------

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


---------------------
Development Toolkits
---------------------

========= ===========================
 Flow      Tools
========= ===========================
 Dev      python, request, logging
 Test     unittest, nose, ipython
 QA       pep8, pylint
 Docs     sphinx, sphinx-autobuild
 DevOps   Makefile
========= ===========================

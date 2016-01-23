####################################
Get Started
####################################

********************
Prequsitions
********************

- Vagrant
- VirtualBox
- Ubuntu 14.04
- Python 2.7.x

********************
Setup
********************

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

*******************
Configuration
*******************

You might need to config two files before starting the app.

- settings.py: set up your ``PLAYER_ID``
- logging.conf: change the logging path if needed

----------------
settings.py
----------------

Config file: ``/path/to/hangmanclient/hangmanbot/settings.py``

- request an account
- update the ``REQUEST_URL`` and ``PLAYER_ID``

::

    #-------------------------------------------------------------------#
    # ACCOUNT SETTINGS

    # request url and play id
    REQUEST_URL = "https://strikingly-hangman.herokuapp.com/game/on"
    PLAYER_ID = "kwailamchan@hotmail.com"


-----------------
logging.conf
----------------- 

logging.conf: ``hangmanbot/conf/logging.conf``

::

   #-------------------------------------------------------------------#
   # LOGGING

   LOGGING_CONF_PATH = PROJECT_ROOT + "/hangmanbot/conf/logging.conf"

If you are not setup the environment as above, you might need to update the log path.

::

    $ vim /path/to/hangmanbot/conf/logging.conf
    

logging.conf

::

    [handler_logFile]
    class=FileHandler
    level=INFO
    formatter=log
    args=('/hangman/hangman_client/logs/hangmanbot.log','a')

    [handler_rotateLogFile]
    class=handlers.RotatingFileHandler
    level=INFO
    formatter=log
    args=('/hangman/hangman_client/logs/hangmanbot.log', 'a', 10*1024*1024, 5)

*********************
Run
*********************

::

    $ source venvs/hangman_client/bin/activate   # activate the virtualenv
    $ cd /path/to/hangmanbot
    $ python -m run

That's it!

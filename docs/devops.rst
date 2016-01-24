##############################
DevOps
##############################

*******************
Devstack
*******************

::

    $ vagrant up
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
    $ pip install -r requirements/docs.txt

    $ mkdir docs
    $ cd docs
    $ sphinx-quickstart
    $ sphinx-autobuild ./ _build/html


*******************
Makefile
*******************

Run Hangmanbot

::

    $ make develop
    $ make hangmanbot.run

Development

::

    $ make develop
    $ make tests
    $ make quality

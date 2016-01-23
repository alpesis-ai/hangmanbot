import logging
import logging.config

import settings

import hangman.hangmanserver
import hangman.hangmanbot
 
logging.config.fileConfig(settings.LOGGING_CONF_PATH)
log = logging.getLogger('root')

def main():

    log.info('Game starts.')
    hangmanServer = hangman.hangmanserver.HangmanServer(settings.REQUEST_URL,
                                                        settings.PLAYER_ID) 
    hangman.hangmanbot.start_game(hangmanServer)
    log.info('Game Ended.')

if __name__ == '__main__':
    main()

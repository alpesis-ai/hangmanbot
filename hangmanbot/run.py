"""
HangmanBot Starts.
"""

import logging
import logging.config

import settings.settings as settings

import hangman.hangmanserver
import hangman.hangmanbot

logging.config.fileConfig(settings.LOGGING_CONF_PATH)
LOG = logging.getLogger('root')


def main():
    """Start a game."""

    LOG.info('Game starts.')
    hangmanServer = hangman.hangmanserver.HangmanServer(settings.REQUEST_URL,
                                                        settings.PLAYER_ID)
    message = hangman.hangmanbot.start_game(hangmanServer)
    LOG.info('Game ended.')


if __name__ == '__main__':
    main()

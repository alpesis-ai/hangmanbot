"""
HangmanBot Starts.
"""

import argparse
import logging
import logging.config

import settings.settings as settings

import hangman.hangmanserver
import hangman.hangmanbot

logging.config.fileConfig(settings.LOGGING_CONF_PATH)
LOG = logging.getLogger('root')


def create_args():
    """Creating arguments."""

    parser = argparse.ArgumentParser()

    parser.add_argument('--sessions', type=int,
                                      default=1,
                                      help='# of sessions to run hangmanbot')

    args = parser.parse_args()
    return args


def run():
    """Start a game."""

    LOG.info('Game starts.')
    hangmanServer = hangman.hangmanserver.HangmanServer(settings.REQUEST_URL,
                                                        settings.PLAYER_ID)
    message = hangman.hangmanbot.start_game(hangmanServer)
    LOG.info('Game ended.')


if __name__ == '__main__':

    args = create_args() 
    for session in range(args.sessions):
        run()

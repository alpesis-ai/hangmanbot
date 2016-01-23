"""
Processing the score and the result.
"""


def get_bestscore(filepath):
    """Returns bestScore from the scorefile.
    """

    score = open(filepath, 'r').readline()
    return int(score)


def save_bestscore(filepath, bestScore):
    """Saving the bestScore.
    """
    open(filepath, 'w').write(bestScore)

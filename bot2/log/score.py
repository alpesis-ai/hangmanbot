import os.path

import settings

def save_best_score(score, filepath=settings.BEST_SCORE_PATH):

    lastScore = get_best_score()
    if score > int(lastScore):
        open(filepath, 'w').write(str(score))
    else:
        pass

def get_best_score(filepath=settings.BEST_SCORE_PATH):

    if os.path.exists(filepath):
        return open(filepath, 'r').readlines()[0].strip()
    else:
        return 1000    

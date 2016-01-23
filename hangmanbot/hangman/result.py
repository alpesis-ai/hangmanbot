def get_bestscore(filepath):
    score = open(filepath, 'r').readline()
    return int(score)

def save_bestscore(filepath, bestScore):
    scorefile = open(filepath, 'w').write(bestScore)

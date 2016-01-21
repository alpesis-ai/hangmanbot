import patterns

def next_word(client, sessionId):
    word = client.next_word(sessionId)
    wordLength = len(word['data']['word'])
    unknownLetters = patterns.unknown_letters(word['data']['word'])
    return word, wordLength, unknownLetters

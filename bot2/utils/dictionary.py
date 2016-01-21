
def split_dict(dictpath):

    words = {}

    dictfile = open(dictpath, 'r')
    for line in dictfile.readlines():
        thisLine = line.strip()
        wordLength = len(thisLine)
        if wordLength > 0:
            if wordLength not in words.keys():
                words[wordLength] = [thisLine]
            else:
                words[wordLength].append(thisLine)

    return words

def split_dicts(dictpaths):

    words = {}

    for dictpath in dictpaths:
        dictfile = open(dictpath, 'r')
        for line in dictfile.readlines():
            thisLine = line.strip()
            wordLength = len(thisLine)
            if wordLength > 0:
                if wordLength not in words.keys():
                    words[wordLength] = [thisLine]
                else:
                    words[wordLength].append(thisLine)

    return words


def split_dict(filepath):
    """
    Splitting the dictionary by the length of word:
    - returns a dictionary of words with {'wordLength': [word1,word2,...]}.
    """

    words = {}
 
    dictfile = open(filepath, 'r')
    for line in dictfile.readlines():
        thisLine = line.strip()
        wordLength = len(line)
        if wordLength not in words.keys():
            words[wordLength] = [thisLine]
        else:
            words[wordLength].append(thisLine)
   
    return words 

def save_dicts(words, outpath):
    """
    Saving the dictionary by the length of words:
    - returns the files with the name 'dictioinary_word_length_xxx'.
    """

    for wordLength in words.keys():
        fileName = 'dictionary_word_length_' + str(wordLength)
        outfile = open(outpath+fileName, 'w')
        for word in words[wordLength]:
            outfile.write(word+"\n")
        outfile.close()


if __name__ == '__main__':
 
    dictpath = './client/files/'
    words = split_dict(dictpath+"dictionary_all.txt")
    save_dicts(words, dictpath) 

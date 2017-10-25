import os
import nltk
import re
from glob import glob
from nltk.probability import FreqDist

#nltk.download() # download punkt
os.chdir('/home/Cacheell/DIGHT360_Fall2017/assignments/Mini-CORE')
register = []
filename = glob('*.txt')
numswearwords = []
numoriginalwords = []
commonword = []


def getfiles():
    for filename in glob('*.txt'):
        wordii= re.search(r'1\+([A-Z][A-Z])\+', filename, re.S)
        register.append(wordii.group(1))


def swearwords():
    for filename in glob('*.txt'):
        with open(filename) as my_file:
            swearwords = 0
            textlen = 0
            my_text = nltk.word_tokenize(my_file.read().lower())
            cusswords = set(['damn', 'shit', 'shits', 'ass', 'asses', 'dammit', 'damnit',
            'shiter', 'bitch', 'bitches', 'hell', 'fuck', 'fucker', 'fucks', 'fucking', 'fag',
            'faggot', 'dicks', 'dick', 'bugger', 'buggers', 'bloddy', 'arse', 'arses'])
            cusscount = len([i for i in my_text if i in cusswords])
            textlen = len(my_text)
            if textlen == 0:
                numswearwords.append('Error')
            else:
                numswearwords.append(cusscount/ textlen)


def originalwords():
    for filename in glob('*.txt'):
        with open(filename) as my_file:
            my_text = nltk.word_tokenize(my_file.read().lower())
            originalwords = len(set(my_text))
            textlen = len(my_text)
            if textlen == 0:
                numoriginalwords.append('Error')
            else:
                numoriginalwords.append(originalwords/ textlen)


def mostcommonwords():
    for filename in glob('*.txt'):
        with open(filename) as my_file:
            my_text = nltk.word_tokenize(my_file.read().lower())
            frequency = FreqDist(my_text)
            commonword.append(frequency.most_common(1))



getfiles()
swearwords()
originalwords()
mostcommonwords()


with open("assignment_5.tsv", "w") as record_file:
    record_file.write('Filename' + '\t' + 'Register' + '\t' + 'Swear Word Percentage' + '\t' + 'Original Word Percentage' + '\t' + 'Most Common words' + '\n')
    for i in range(len(filename)):
        record_file.write(filename[i] + '\t' + register[i] + '\t' + str(numswearwords[i]) + '\t' + str(numoriginalwords[i]) + '\t' + str(commonword[i])+ '\n')



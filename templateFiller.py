from itertools import chain
import random
import math
import re

with open("hypotheses.txt", 'r') as f:
    linesText = f.readlines()

with open("input.txt", 'r') as f:
    linesData = f.readlines()

def replaceToken(i, word):
    word = word.strip("<").strip(">").split("_")
    pattern = re.compile(word[0] + "_.*_" + word[2])

    #replace with number
    tag = ""
    for k in range(len(linesData[i].split())):
        if pattern.match(linesData[i].split()[k]):
            tag = linesData[i].split()[k+1]

    return tag

text0 = ""
text1 = ""
for i in range(len(linesData)):
    new_str = ""
    new_str2 = ""

    for word in linesText[i].split():
        word2 = word
        if word[0] == "<":
            word2 = replaceToken(i, word)

        new_str2 += word2.strip() + " "
    
    text1 += new_str2 + "\n"

with open("templatized.text", 'w') as f:
    f.write(text1)

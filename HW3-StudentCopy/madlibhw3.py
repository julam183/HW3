# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text

import nltk
from nltk.book import *

text = text2[:150]


print("START*******")


noun = input("Please enter a noun: ")
verb = input("Please enter a verb: ")
adjective = input("Please enter an adjective: ")
adverb = input("Please enter an adverb: ")
number = input("Please enter a number: ")

madlib = ''
original = ''
for n in range(150):
    tag = nltk.pos_tag(text[n])
    print (tag)
    if tag[0][1] == 'NN':
        madlib += noun + " "
    elif tag[0][1] == 'VB':
        madlib += verb + " "
    elif tag[0][1] == 'JJ':
        madlib += adjective + " "
    elif tag[0][1] == 'RB':
        madlib += adverb + " "
    elif tag[0][1] == 'NCD':
        madlib += number + " "
    else:
        madlib += text[n] + " "
    original += text[n] + " "

print (original)
print (madlib)

print("\n\nEND*******")

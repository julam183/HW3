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
from nltk.tag import pos_tag, map_tag
import random


text = text2[:150]


print("START*******")


noun = input("Please enter a noun: ")
verb = input("Please enter a verb: ")
adjective = input("Please enter an adjective: ")
adverb = input("Please enter an adverb: ")
number = input("Please enter a number: ")

madlib = ''
original = ''
tag = pos_tag(text)
tag = [(word, map_tag('en-ptb', 'universal', tag)) for word, tag in tag]
for pair in tag:
    id = pair[1]
    if id == ('NOUN'):
        if (random.random() < .15):
            madlib += noun + " "
        else:
            madlib += pair[0] + " "
    elif id == ('VERB'):
        if (random.random() < .1):
            madlib += verb + " "
        else:
            madlib += pair[0] + " "
    elif id == ('ADJ'):
        if (random.random() < .1):
            madlib += adjective + " "
        else:
            madlib += pair[0] + " "
    elif id == ('ADV'):
        if (random.random() < .1):
            madlib += adverb + " "
        else:
            madlib += pair[0] + " "
    elif id == ('NUM'):
        if (random.random() < .1):
            madlib += number + " "
        else:
            madlib += pair[0] + " "
    else:
        madlib += pair[0] + " "
    original += pair[0] + " "
print (original)
print (madlib)

print("\n\nEND*******")

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:06:16 2017

@author: Vipin
"""

import csv, re, nltk
from nltk import word_tokenize
from nltk.collocations import *

with open("D:/Python/Consumer Complaints/Consumer_Complaints_CreditCard.csv", 'r') as file:
  complaints = list(csv.reader(file))
  file.close()

compClean = []
for i in range(len(complaints)):
    tokens = re.sub("[^A-Za-z0-9()'.]+", " ", complaints[i][5])
    tokens = re.sub('!', ".", tokens)
    compClean.append(tokens)


from nltk.corpus import webtext
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import BigramAssocMeasures
words = [w.lower() for w in webtext.words('D:/Python/Consumer Complaints/complaintsDump.txt')]
bcf = BigramCollocationFinder.from_words(words)

#from nltk.collocations import TrigramCollocationFinder
#from nltk.metrics import TrigramAssocMeasures
#tcf = TrigramCollocationFinder.from_words(words)
#tcf.nbest(TrigramAssocMeasures.likelihood_ratio, 4)

from nltk.corpus import stopwords
stopset = set(stopwords.words('english'))
filter_stops = lambda w: len(w) < 3 or w in stopset
bcf.apply_word_filter(filter_stops)
collocations = bcf.nbest(BigramAssocMeasures.likelihood_ratio, 50)

newText = 'a credit card is issued to me'
tokens = re.sub(" ".join(collocations[1]), "-".join(collocations[1]), newText)




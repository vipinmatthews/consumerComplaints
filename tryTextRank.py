# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:06:16 2017

@author: Vipin
"""


import csv, re
from nltk import word_tokenize
from gensim.summarization import summarize

with open("D:/Python/Consumer Complaints/Consumer_Complaints_CreditCard.csv", 'r') as file:
  complaints = list(csv.reader(file))
  file.close()

replacement_patterns = [
	(r'won\'t', 'will not'),
	(r'can\'t', 'cannot'),
   (r'\'m', 'am'),
	(r'ain\'t', 'is not'),
	(r'(\w+)\'ll', '\g<1> will'),
   (r'\'ll', 'will'),
	(r'(\w+)n\'t', '\g<1> not'),
	(r'(\w+)\'ve', '\g<1> have'),
   (r'\'ve', 'have'),
	(r'(\w+)\'re', '\g<1> are'),
   (r'\'re', 'are'),
]

class RegexpReplacer(object):
	""" Replaces regular expression in a text.
	>>> replacer = RegexpReplacer()
	>>> replacer.replace("I should've done that thing I didn't do")
	'I should have done that thing I did not do'
	"""
	def __init__(self, patterns=replacement_patterns):
		self.patterns = [(re.compile(regex), repl) for (regex, repl) in patterns]
	
	def replace(self, text):
		s = text
		
		for (pattern, repl) in self.patterns:
			s = re.sub(pattern, repl, s)
		
		return s

compClean = []
for i in range(len(complaints)):
    replacer = RegexpReplacer()
    tokens = replacer.replace(complaints[i][5])
    tokens = re.sub("[^A-Za-z0-9()'.]+", " ", tokens)
    tokens = re.sub('!', ".", tokens)
    compClean.append(tokens)
    
  
compSummary = []
for i in range(len(compClean)):
    try:
        compSummary.append(summarize(compClean[i], ratio = 0.1))
    except:
        compSummary.append("Unable to Summarize")
    
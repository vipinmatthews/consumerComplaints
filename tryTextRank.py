import csv, re
from gensim.summarization import summarize
from gensim.summarization import keywords

with open("Consumer_Complaints_CreditCard.csv", 'r') as file:
  complaints = list(csv.reader(file))

compClean = []
for i in range(len(complaints)):
    tokens = re.sub("[^A-Za-z0-9()'.]+", " ", complaints[i][5])
    tokens = re.sub('!', ".", tokens)
    compClean.append(tokens)
  
compSummary = []
for i in range(len(compClean)):
    try:
        compSummary.append(summarize(compClean[i], ratio = 0.1))
    except:
        compSummary.append("Unable to Summarize")



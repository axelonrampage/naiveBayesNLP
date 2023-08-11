import pickle
import os
import csv
from collections import Counter

dbfile = open('../../../dataset/classic4/experiment1/frequency/training/trainingtermfrequency', 'rb')
classFerq=pickle.load(dbfile)
dbfile1 = open('../../../dataset/classic4/experiment1/frequency/testing/testingtermfrequency', 'rb')
classFerq1=pickle.load(dbfile1)

totalfrequency=classFerq+classFerq1
with open('../../../dataset/classic4/experiment1/frequency/datasettermfrequency', 'wb') as dp:
   pickle.dump(totalfrequency, dp)
# print(len(Counter(totalfrequency).keys())) # equals to list(set(words))
#print(Counter(classFerq).values()) # counts the elements' frequency

# This prints 3 most frequent characters 
#for letter, count in totalfrequency.most_common(100):
#    print('%s: %d' % (letter, count))
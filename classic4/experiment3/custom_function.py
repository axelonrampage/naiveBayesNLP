from __future__ import print_function
import re
import os
import random
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from collections import Counter


ps = PorterStemmer()

def documentAfterToken(word,document):
    split_sentence = document.split(word,1)
    if 1<len(split_sentence):
        document=split_sentence[1];
    else:
        document=split_sentence[0];
    return document

def extractEmail(document):
    reg=r'(?:\.?)([\w\-_+#~!$&\'\.]+(?<!\.)(@|[ ]\(?[ ]?(at|AT)[ ]?\)?[ ])(?<!\.)[\w]+[\w\-\.]*\.[a-zA-Z-]{2,3})(?:[^\w])'
    matches = re.findall(reg, document)
    get_first_group = lambda y: list(map(lambda x: x[0], y))
    emailArray = get_first_group(matches)
    
##    emailArray = re.findall(r'[\w\d\.-]+@[\w\.-]+', document)
    return emailArray

def stopWordRemovalAndStemming(document,language):
    filtered_sentence = []
    stop_words = set(stopwords.words(language))
    word_tokens = word_tokenize(document)
    for w in word_tokens:
            if w not in stop_words:                
                    filtered_sentence.append(ps.stem(w))
    return filtered_sentence

def removeToken(word_tokens,token):
    filtered_sentence = []
    for w in word_tokens:
            if w not in token:                
                    filtered_sentence.append(ps.stem(w))
    return filtered_sentence

def removeEmail(document):
    reg=r'(?:\.?)([\w\-_+#~!$&\'\.]+(?<!\.)(@|[ ]\(?[ ]?(at|AT)[ ]?\)?[ ])(?<!\.)[\w]+[\w\-\.]*\.[a-zA-Z-]{2,3})(?:[^\w])'
    emailRemovedDocument =re.sub(reg, '', document)
##    emailRemovedDocument =re.sub(r'[\w\.-]+@[\w\.-]+', '', document)
    return emailRemovedDocument

def removeNAS(document):
    reg=r'[^A-Za-z]+'
    emailRemovedDocument =re.sub(reg, ' ', document)
##    emailRemovedDocument =re.sub(r'[\w\.-]+@[\w\.-]+', '', document)
    return emailRemovedDocument


## Unicode Lower case

def unicodeLowerCase(document):
    unicode_from_document = document.encode();
    unicode_from_document.lower()
    return unicode_from_document

## Finding unique item from the list.

def findUnique(listItem):
    listItems = list(set(listItem))
    return listItems

## Making New Directory

def makeDirectory(path,dataset):
    files = os.listdir(path)
    for name in files:
        directoryTraining="output/"+dataset+"/training/"+name
        directoryTesting="output/"+dataset+"/testing/"+name
        if not os.path.exists(directoryTraining):
            os.makedirs(directoryTraining)
        if not os.path.exists(directoryTesting):
            os.makedirs(directoryTesting)
    return True

## For partitioning list in 'n' equal partition

def partition (list_in, n):
    random.shuffle(list_in)
    return [list_in[i::n] for i in range(n)]

## For finding file name of given directory

def findFileName(path):
    files = os.listdir(path)
    for name in files:
        print(name)
    return name


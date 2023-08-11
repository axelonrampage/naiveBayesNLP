import re
import pickle
import os
from collections import Counter
import nltk

class FerquencyFunction:

##    def __init__(self):
##        print('constructer called')

    def termFrequency(self,listItem,directory,docType,folderName,fileName):
##        outFileName='output/20_newsgroups/frequency/training/alt.atheism/'+str(fileName)
        outFilePath=directory+'/'+docType+'/'+folderName
        outFileName=outFilePath+'/'+str(fileName)
        termFreq=Counter(listItem)
        with open(outFileName, 'wb') as fp:
            pickle.dump(termFreq, fp)
        if(os.path.exists(outFilePath+"/classtermfrequency")):
            classtermfrequency = open(outFilePath+'/classtermfrequency', 'rb')     
            ctf = pickle.load(classtermfrequency)
            ctf = ctf + termFreq
        else :
            ctf = termFreq
        with open(outFilePath+'/classtermfrequency', 'wb') as dp:
            pickle.dump(ctf, dp)

        return ctf


    def termFrequencyRatio(self, listItem, directory, docType, folderName, fileName):
    ##        outFileName='output/20_newsgroups/frequency/training/alt.atheism/'+str(fileName)
        outFilePath = directory + '/' + docType + '/' + folderName
        outFileName = outFilePath + '/' + str(fileName)
        termFreq = Counter(listItem)
        # print("TermFreq",termFreq)
        counterDict={}
        documentFrequency=sum(termFreq.values())
        for ke,val in termFreq.items():
            ratioVal=val*(100/documentFrequency)
            counterDict.update({ke:ratioVal})
        counterDict1=Counter(counterDict)
        with open(outFileName, 'wb') as fp:
            pickle.dump(counterDict1, fp)
        if (os.path.exists(outFilePath + "/classtermfrequency")):
            classtermfrequency = open(outFilePath + '/classtermfrequency', 'rb')
            ctf = pickle.load(classtermfrequency)
            ctf = ctf + counterDict1
        else:
            ctf = counterDict1
        with open(outFilePath + '/classtermfrequency', 'wb') as dp:
            pickle.dump(ctf, dp)

        return ctf

import pickle
import os
import csv
import math
from collections import Counter

inputDirectory='../../../dataset/classic4/experiment3/frequencyRatio/training'
outputCounterDirectory='../../../dataset/classic4/experiment3/classProbability/counterforth'
#outputExcelDirectory='output/classic4/classProbability/excel'
docTypeList = os.listdir(inputDirectory)

with open(inputDirectory+'/'+'trainingtermfrequency', 'rb') as fp:
    datasetFerq=pickle.load(fp)

Nv=len(datasetFerq.keys())

for docType in docTypeList:
    Ni=0
    termProbabilityDisc={}
    if docType!='trainingtermfrequency':
        classPath=inputDirectory+'/'+docType+'/classtermfrequency'
        with open(classPath, 'rb') as fp:
            classFerq=pickle.load(fp)
        Ni=sum(classFerq.values())
        outputCounterFilepath=outputCounterDirectory+'/'+docType+'termprobability'
#        outputExcelFilepath=outputExcelDirectory+'/'+docType+'termprobability.csv'
        for term in datasetFerq.keys():
            termClassProbability=0
            if classFerq[term]>0:
                termProbability=(classFerq[term]+1)/(Nv+Ni)
#                termClassProbability=math.log(termProbability)            
            termProbabilityDisc.update({term : termProbability})
        with open(outputCounterFilepath, 'wb') as fp:
            pickle.dump(termProbabilityDisc, fp)
#        with open(outputExcelFilepath, 'w') as exf:
#            wr = csv.writer(exf, dialect='excel')
#            wr.writerows(termProbabilityDisc)

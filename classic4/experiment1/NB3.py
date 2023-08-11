import pickle
import os
import csv
from collections import Counter

#inputDirectory='output/20_newsgroups/frequency'
#outputCounterDirectory='output/20_newsgroups/frequencyWithIndex/counter'
#outputExcelDirectory='output/20_newsgroups/frequencyWithIndex/excel'
#docTypeList = os.listdir(inputDirectory)


inputDirectory='../../../dataset/classic4/experiment1/frequency'
outputCounterDirectory='../../../dataset/classic4/experiment1/frequencyWithIndex/counter'
outputExcelDirectory='../../../dataset/classic4/experiment1/frequencyWithIndex/excel'
docTypeList = os.listdir(inputDirectory)


with open(inputDirectory+'/'+'datasettermfrequency', 'rb') as fp:
    datasetFerq=pickle.load(fp)
v=sorted(datasetFerq .keys())
idDict={item:i for i,item in enumerate(v) }
idFCount={item:0 for i,item in enumerate(v) }

finalDataTypeList=[(idDict[item[0]],item[0],item[1]) for item in datasetFerq.items()]
with open(inputDirectory+'/idlist.csv', 'w') as oedf:
    wr = csv.writer(oedf, dialect='excel')
    wr.writerows(finalDataTypeList)
    for docType in docTypeList:
        if docType!='datasettermfrequency':
            idFDocTypeCount={item:0 for i,item in enumerate(v) }
            folderNameList=os.listdir(inputDirectory+'/'+docType)
            for folderName in folderNameList:
                if folderName!=docType+'termfrequency':
                    classPath=inputDirectory+'/'+docType+'/'+folderName+'/'
                    outputCounterClassPath=outputCounterDirectory+'/'+docType+'/'+folderName+'/'
                    outputExcelClassPath=outputExcelDirectory+'/'+docType+'/'+folderName+'/'
                    files = os.listdir(classPath)
                    for targetfile in files:
                        if targetfile!='classtermfrequency':
                            filepath=classPath+targetfile
                            outputCounterFilepath=outputCounterClassPath+targetfile
                            outputExcelFilepath=outputExcelClassPath+targetfile+'.csv'
                            docTypetermfrequency = open(filepath, 'rb')     
                            fileTermFreq = pickle.load(docTypetermfrequency)
                            fileList=[(idDict[item[0]],item[0],item[1]) for item in fileTermFreq.items()]
##                            print(filepath)
                            with open(outputCounterFilepath, 'wb') as fp:
                                pickle.dump(fileList, fp)
                            with open(outputExcelFilepath, 'w') as exf:
                                wr = csv.writer(exf, dialect='excel')
                                wr.writerows(fileList)
                            for element in fileTermFreq.items():
                                idFCount[element[0]]=idFCount[element[0]]+1
                                idFDocTypeCount[element[0]]=idFDocTypeCount[element[0]]+1
##                                print(element[0],element[1],idFCount[element[0]])
            dataTypeList=[(idDict[item[0]],item[0],item[1],idFCount[item[0]]) for item in datasetFerq.items()]
            with open(outputCounterDirectory+'/'+docType+'/'+docType+'inverselist', 'wb') as ocdp:
                pickle.dump(dataTypeList, ocdp)
            with open(outputExcelDirectory+'/'+docType+'/'+docType+'inverselist.csv', 'w') as oedf:
                wr = csv.writer(oedf, dialect='excel')
                wr.writerows(dataTypeList)
finalDataTypeList=[(idDict[item[0]],item[0],item[1],idFCount[item[0]]) for item in datasetFerq.items()]
with open(outputCounterDirectory+'/inverselist', 'wb') as ocdp:
    pickle.dump(finalDataTypeList, ocdp)
with open(outputExcelDirectory+'/inverselist.csv', 'w') as oedf:
    wr = csv.writer(oedf, dialect='excel')
    wr.writerows(finalDataTypeList)



##with open(outputDirectory+'/'+'datasettermfrequency', 'wb') as fp:
##    pickle.dump(cft, fp)

##v=sorted(cft.keys())
##idDict={item[0]:i for i,item in enumerate(v) }

#print(idDict)
##bresult=[(idDict[item[0]],item[0],item[1]) for item in bCounter.items()]
##aresult=[(idDict[item[0]],item[0],item[1]) for item in aCounter.items() ]

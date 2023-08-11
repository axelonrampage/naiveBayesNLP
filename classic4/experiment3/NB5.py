import pickle
import os
import csv
from collections import Counter
mostCommon=100
inputDirectory='../../../dataset/classic4/experiment3/frequencyRatio/testing'
# cacmTermProbFilePath='../../../dataset/classic4/experiment3/classProbability/countersecond/cacmtermprobability'
# cisiTermProbFilePath='../../../dataset/classic4/experiment3/classProbability/countersecond/cisitermprobability'
# cranTermProbFilePath='../../../dataset/classic4/experiment3/classProbability/countersecond/crantermprobability'
# # medTermProbFilePath='../../../dataset/classic4/experiment3/classProbability/countersecond/medtermprobability'
# coursetermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/coursetermprobability'
# departmenttermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/departmenttermprobability'
# facultytermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/facultytermprobability'
# projecttermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/projecttermprobability'
# stafftermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/stafftermprobability'
# studenttermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/studenttermprobability'
cacmtermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/cacmtermprobability'
cisitermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/cisitermprobability'
crantermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/crantermprobability'
medtermprobability='../../../dataset/classic4/experiment3/classProbability/counterforth/medtermprobability'
outputDirectory = '../../../dataset/classic4/experiment3/selectedFeatures/'+str(mostCommon)+'Features'
docTypeList = os.listdir(inputDirectory)

with open(cacmtermprobability, "rb") as cacmtermprobabilityFile:
    cacmtermprobabilityFileTermProb = pickle.load(cacmtermprobabilityFile)
cacmtermprobabilityFile = {x: y for x, y in cacmtermprobabilityFileTermProb.items() if y != 0}
cacmtermprobabilityFile = dict(Counter(cacmtermprobabilityFileTermProb).most_common(mostCommon))
with open(cisitermprobability, "rb") as cisitermprobabilityFile:
    cisitermprobabilityFileTermProb = pickle.load(cisitermprobabilityFile)
cisitermprobabilityFile = {x: y for x, y in cisitermprobabilityFileTermProb.items() if y != 0}
cisitermprobabilityFile = dict(Counter(cisitermprobabilityFileTermProb).most_common(mostCommon))
with open(crantermprobability, "rb") as crantermprobabilityFile:
    crantermprobabilityFileTermProb = pickle.load(crantermprobabilityFile)
crantermprobabilityFile = {x: y for x, y in crantermprobabilityFileTermProb.items() if y != 0}
crantermprobabilityFile = dict(Counter(crantermprobabilityFileTermProb).most_common(mostCommon))
with open(medtermprobability, "rb") as medtermprobabilityFile:
    medtermprobabilityFileTermProb = pickle.load(medtermprobabilityFile)
medtermprobabilityFile = {x: y for x, y in medtermprobabilityFileTermProb.items() if y != 0}
medtermprobabilityFile = dict(Counter(medtermprobabilityFileTermProb).most_common(mostCommon))

for docType in docTypeList:
    if docType!='testingtermfrequency':
        classPath=inputDirectory+'/'+docType
        files = os.listdir(classPath)
#        outputDict={'File Name':{'cacm','cisi','cran','med','max','result class','result'}}
        outputCounterFilepath=outputDirectory+'/'+docType
        outputExcelFilepath=outputDirectory+'/'+docType+'.csv'
        outputDict={}
        outputList=[]
        for targetfile in files:
            if targetfile!='classtermfrequency':
                filecacmtermprobability = 0
                filecisitermprobability = 0
                filecrantermprobability = 0
                filemedtermprobability = 0
                filePath=classPath+'/'+targetfile
                with open(filePath, 'rb') as fp:
                    fileTermList=pickle.load(fp)
                
                for fileTerm in fileTermList.keys():
                    # if fileTerm in cacmTermProb:
                    #     fileCacm=fileCacm + cacmTermProb[fileTerm]
                    # if fileTerm in cisiTermProb:
                    #     fileCisi=fileCisi + cisiTermProb[fileTerm]
                    # if fileTerm in cranTermProb:
                    #     fileCran=fileCran + cranTermProb[fileTerm]
                    # if fileTerm in medTermProb:
                    #     fileMed=fileMed + medTermProb[fileTerm]
                    if fileTerm in cacmtermprobabilityFile:
                        filecacmtermprobability = filecacmtermprobability + cacmtermprobabilityFile[fileTerm]
                    if fileTerm in cisitermprobabilityFile:
                        filecisitermprobability = filecisitermprobability + cisitermprobabilityFile[fileTerm]
                    if fileTerm in crantermprobabilityFile:
                        filecrantermprobability = filecrantermprobability + crantermprobabilityFile[fileTerm]
                    if fileTerm in medtermprobabilityFile:
                        filemedtermprobability = filemedtermprobability + medtermprobabilityFile[fileTerm]

                maxArray=[]
                maxValue=0
                # if fileCacm !=0:
                #     maxArray.append(fileCacm)
                # if fileCisi !=0:
                #     maxArray.append(fileCisi)
                # if fileCran !=0:
                #     maxArray.append(fileCran)
                # if fileCacm !=0:
                #     maxArray.append(fileCacm)
                # if fileMed !=0:
                #     maxArray.append(fileMed)
                if filecacmtermprobability != 0:
                    maxArray.append(filecacmtermprobability)
                if filecisitermprobability != 0:
                    maxArray.append(filecisitermprobability)
                if filecrantermprobability != 0:
                    maxArray.append(filecrantermprobability)
                if filemedtermprobability != 0:
                    maxArray.append(filemedtermprobability)

                if len(maxArray) != 0:
                    maxValue=max(maxArray)
                    
                    # if maxValue == fileCacm:
                    #     outputClass='cacm'
                    # elif maxValue == fileCisi:
                    #     outputClass='cisi'
                    # elif maxValue == fileCran:
                    #     outputClass='cran'
                    # elif maxValue == fileMed:
                    #     outputClass='med'
                    if maxValue == filecacmtermprobability:
                        outputClass = 'cacm'
                    elif maxValue == filecisitermprobability:
                        outputClass = 'cisi'
                    elif maxValue == filecrantermprobability:
                        outputClass = 'cran'
                    elif maxValue == filemedtermprobability:
                        outputClass = 'med'


                    if outputClass == docType:
                        outputValue=True
                    else :
                        outputValue=False
                else :
                    outputClass='undifined'
                    outputValue='undifined'
                outputDict.update({targetfile:{'cacm':filecacmtermprobability,'cisi':filecisitermprobability,
                                               'cran':filecrantermprobability,'med':filemedtermprobability,

                                        'maxValue' : maxValue,'result class' : outputClass,'result' : outputValue}})
                outputList.append((filecacmtermprobability,filecisitermprobability,
                                   filecrantermprobability,
                                   filemedtermprobability,
                                   maxValue,outputClass,outputValue))
        with open(outputCounterFilepath, 'wb') as fp:
            pickle.dump(outputDict, fp)
        with open(outputExcelFilepath, 'w') as exf:
            wr = csv.writer(exf, dialect='excel')
            wr.writerows(outputList)
print('DOne')
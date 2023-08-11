import pickle
# import os
import json
mostCommon=100
inputDirectory='../../../dataset/classic4/experiment3/selectedFeatures/'+str(mostCommon)+'Features'
resultDir='../../../dataset/classic4/experiment3/result/'+str(mostCommon)+'Features/result'

classes=['cacm','cisi','cran','med']
arrLen=len(classes)
confussionMatrix=arr = [[0 for i in range(arrLen)] for j in range(arrLen)]
for className in classes:
    inputPath=inputDirectory+'/'+className
    with open(inputPath, 'rb') as inputClass:
        inputClassResult=pickle.load(inputClass)
    row=classes.index(className)
    for classFileName,resultData in inputClassResult.items():
        if(resultData['result class']!='undifined'):
            col=classes.index(resultData['result class'])
            confussionMatrix[row][col]=confussionMatrix[row][col]+1
with open(resultDir,"w") as f:
    f.write(json.dumps(confussionMatrix))
# print(confussionMatrix)
for itemss in confussionMatrix:
    print(itemss)
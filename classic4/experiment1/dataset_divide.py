import random,os
import shutil

path = '../../../dataset/classic4/'
# print(os.listdir(path))
for folders in os.listdir(path):
    print(folders)
    fileDir=path+folders+'/'
    files=os.listdir(fileDir)
    random.shuffle(files)
    cont=int(len(files)*.7)
    testingPath='../../dataset/classic4/main/testing/'
    trainingPath='../../dataset/classic4/main/training/'
    trainPath=trainingPath+folders+'/'
    testPath=testingPath+folders+'/'
    trainingfiles=files[:cont]
    testingfiles=files[cont:]
    for targetfile in testingfiles:
        filePath=path+folders+'/'+targetfile
        shutil.copy2(filePath, testPath)
    for targetfile in trainingfiles:
        filePath=path+folders+'/'+targetfile
        shutil.copy2(filePath, trainPath)

## File Transfer End
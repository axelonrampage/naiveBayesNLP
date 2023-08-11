import custom_function
from FerquencyFunction import *
import inspect
from collections import Counter
import nltk


inputDirectory='../../../dataset/classic4/main'
outputFileDirectory='../../../dataset/classic4/experiment3/preprocessed'
outputDirectory='../../../dataset/classic4/experiment3/frequencyRatio'
outputEmailDirectory='../../../dataset/classic4/experiment3/email'
docTypeList = os.listdir(inputDirectory)


for docType in docTypeList:
    folderNameList=os.listdir(inputDirectory+'/'+docType)
    for folderName in folderNameList:
        trainingPath=inputDirectory+'/'+docType+'/'+folderName+'/'
        files = os.listdir(trainingPath)
        print(folderName)
        for targetfile in files:
            filepath=trainingPath+targetfile

            fileData = open(filepath, "r",errors='ignore')
            sentence=fileData.read()
            word='Lines:'
            document= custom_function.documentAfterToken(word,sentence)
#            emailArray=custom_function.extractEmail(document)
#            mainEmailArray={}
#            mainEmailArray=emailArray
#            with open(outputEmailDirectory+'/'+docType+'/'+folderName+'/'+targetfile, 'wb') as fp:
#                pickle.dump(mainEmailArray, fp)
#
#
#            emailRemoved = custom_function.removeEmail(document)
            numberAndSpecialSymbolRemoved = custom_function.removeNAS(document)

            numberAndSpecialSymbolRemoved=numberAndSpecialSymbolRemoved.lower()

            stemmedArray = custom_function.stopWordRemovalAndStemming(numberAndSpecialSymbolRemoved,'english')
            # print("Length Before",len(stemmedArray))
            stemmedArray= [word for word in stemmedArray if len(word)>3]
            # print('Length After',len(stemmedArray))
            saveFile=open(outputFileDirectory+'/'+docType+'/'+folderName+'/'+targetfile,'w')
            saveFile.write(str(stemmedArray))

            A=FerquencyFunction()
            A.termFrequencyRatio(stemmedArray,outputDirectory,docType,folderName,targetfile)
        outFilePath=outputDirectory+'/'+docType+'/'+folderName
        classtermfrequency = open(outFilePath+'/classtermfrequency', 'rb')
        ctf = pickle.load(classtermfrequency)
        if(os.path.exists(outputDirectory+'/'+docType+'/'+docType+'termfrequency')):
            docTypetermfrequency = open(outputDirectory+'/'+docType+'/'+docType+"termfrequency", 'rb')
            dtf = pickle.load(docTypetermfrequency)
            dtf = dtf + ctf
        else :
            dtf = ctf
        with open(outputDirectory+'/'+docType+'/'+docType+"termfrequency", 'wb') as dp:
            pickle.dump(dtf, dp)



##dbfile = open('output/20_newsgroups/frequency/training/alt.atheism/classtermfrequency', 'rb')
##classFerq=pickle.load(dbfile)
##print(len(Counter(classFerq).keys())) # equals to list(set(words))
##print(Counter(classFerq).values()) # counts the elements' frequency

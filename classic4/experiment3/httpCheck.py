import custom_function
from FerquencyFunction import *
import inspect
from collections import Counter
import nltk
from bs4 import BeautifulSoup

inputDirectory='../../dataset/webkb/main'
outputFileDirectory='../../dataset/webkb/preprocessed'
outputDirectory='../../dataset/webkb/frequency'
outputEmailDirectory='../../dataset/webkb/email'
docTypeList = os.listdir(inputDirectory)
# CLEANR = re.compile('<.*?>|&([a-z0-9]+|#[0-9]{1,6}|#x[0-9a-f]{1,6});')

fnVar=''
# def cleanhtml(raw_html):
#   cleantext = re.sub(CLEANR, '', raw_html)
#   return cleantext
v=''
totalcount=0
Htmlcount=0
for docType in docTypeList:
    folderNameList=os.listdir(inputDirectory+'/'+docType)
    for folderName in folderNameList:
        trainingPath=inputDirectory+'/'+docType+'/'+folderName+'/'
        files = os.listdir(trainingPath)
        print(folderName)

        for targetfile in files:
            totalcount=totalcount+1
            filepath=trainingPath+targetfile

            fileData = open(filepath, "r",errors='ignore')
            sent=fileData.read()
            sentence=BeautifulSoup(sent, "lxml").text
            print("Length Before",len(sent))

            print("Length After",len(sentence))

            # print(len(sentence))
            # print("+++++++++++++++++++++++AFter only HTML REMOVAL",sentence)
            word='Last-Modified:'
            document= custom_function.documentAfterToken(word,sentence)
            # print(len(document))
            emailArray=custom_function.extractEmail(document)
            mainEmailArray={}
            mainEmailArray=emailArray
           # with open(outputEmailDirectory+'/'+docType+'/'+folderName+'/'+targetfile, 'wb') as fp:
           #     pickle.dump(mainEmailArray, fp)


            emailRemoved = custom_function.removeEmail(document)
            # print(emailRemoved)
            # exit()
            numberAndSpecialSymbolRemoved = custom_function.removeNAS(emailRemoved)

            numberAndSpecialSymbolRemoved=numberAndSpecialSymbolRemoved.lower()

            stemmedArray = custom_function.stopWordRemovalAndStemming(numberAndSpecialSymbolRemoved,'english')
            # print('Before',len(stemmedArray))

            stemmedArray=[word for word in stemmedArray if len(word)>2]
            # print('Final',len(stemmedArray))
            # saveFile=open(outputFileDirectory+'/'+docType+'/'+folderName+'/'+targetfile,'w')
            # saveFile.write(str(stemmedArray))

            if 'html' in stemmedArray:
                print("Found")
                # print(filepath)
            #     Htmlcount=Htmlcount+1
# print("HTML COUNT",Htmlcount)
# print("TOTAL COUNT",totalcount)
            # A=FerquencyFunction()
            # A.termFrequency(stemmedArray,outputDirectory,docType,folderName,targetfile)

        # outFilePath=outputDirectory+'/'+docType+'/'+folderName
        # classtermfrequency = open(outFilePath+'/classtermfrequency', 'rb')
        # ctf = pickle.load(classtermfrequency)
        # if(os.path.exists(outputDirectory+'/'+docType+'/'+docType+'termfrequency')):
        #     docTypetermfrequency = open(outputDirectory+'/'+docType+'/'+docType+"termfrequency", 'rb')
        #     dtf = pickle.load(docTypetermfrequency)
        #     dtf = dtf + ctf
        # else :
        #     dtf = ctf


##dbfile = open('output/20_newsgroups/frequency/training/alt.atheism/classtermfrequency', 'rb')
##classFerq=pickle.load(dbfile)
##print(len(Counter(classFerq).keys())) # equals to list(set(words))
##print(Counter(classFerq).values()) # counts the elements' frequency

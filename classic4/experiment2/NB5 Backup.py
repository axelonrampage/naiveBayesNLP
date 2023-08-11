import pickle
import os
import csv
from collections import Counter

inputDirectory = '../dataset/20News/Frequency/Testing'
# cacmTermProbFilePath = '../dataset/20News/classProbability/counterforth/cacmtermprobability'
# cisiTermProbFilePath = '../dataset/20News/classProbability/counterforth/cisitermprobability'
# cranTermProbFilePath = '../dataset/20News/classProbability/counterforth/crantermprobability'
# medTermProbFilePath = '../dataset/20News/classProbability/counterforth/medtermprobability'
alt_atheismtermprobability='../dataset/20News/classProbability/counterforth/alt.atheismtermprobability'
comp_graphicstermprobability='../dataset/20News/classProbability/counterforth/comp.graphicstermprobability'
comp_os_ms_windows_misctermprobability='../dataset/20News/classProbability/counterforth/comp.os.ms-windows.misctermprobability'
comp_sys_ibm_pc_hardwaretermprobability='../dataset/20News/classProbability/counterforth/comp.sys.ibm.pc.hardwaretermprobability'
comp_sys_mac_hardwaretermprobability='../dataset/20News/classProbability/counterforth/comp.sys.mac.hardwaretermprobability'
comp_windows_xtermprobability='../dataset/20News/classProbability/counterforth/comp.windows.xtermprobability'
misc_forsaletermprobability='../dataset/20News/classProbability/counterforth/misc.forsaletermprobability'
rec_autostermprobability='../dataset/20News/classProbability/counterforth/rec.autostermprobability'
rec_motorcyclestermprobability='../dataset/20News/classProbability/counterforth/rec.motorcyclestermprobability'
rec_sport_baseballtermprobability='../dataset/20News/classProbability/counterforth/rec.sport.baseballtermprobability'
rec_sport_hockeytermprobability='../dataset/20News/classProbability/counterforth/rec.sport.hockeytermprobability'
sci_crypttermprobability='../dataset/20News/classProbability/counterforth/sci.crypttermprobability'
sci_electronicstermprobability='../dataset/20News/classProbability/counterforth/sci.electronicstermprobability'
sci_medtermprobability='../dataset/20News/classProbability/counterforth/sci.medtermprobability'
sci_spacetermprobability='../dataset/20News/classProbability/counterforth/sci.spacetermprobability'
soc_religion_christiantermprobability='../dataset/20News/classProbability/counterforth/soc.religion.christiantermprobability'
talk_politics_gunstermprobability='../dataset/20News/classProbability/counterforth/talk.politics.gunstermprobability'
talk_politics_mideasttermprobability='../dataset/20News/classProbability/counterforth/talk.politics.mideasttermprobability'
talk_politics_misctermprobability='../dataset/20News/classProbability/counterforth/talk.politics.misctermprobability'
talk_religion_misctermprobability='../dataset/20News/classProbability/counterforth/talk.religion.misctermprobability'
outputDirectory = '../dataset/20News/result/selectedtokensecond'
docTypeList = os.listdir(inputDirectory)

# with open(cacmTermProbFilePath, 'rb') as cacm:
#     cacmTermProb = pickle.load(cacm)
# cacmTermProb = {x: y for x, y in cacmTermProb.items() if y != 0}
# cacmTermProb = dict(Counter(cacmTermProb).most_common(100))
#
# with open(cisiTermProbFilePath, 'rb') as cisi:
#     cisiTermProb = pickle.load(cisi)
# cisiTermProb = {x: y for x, y in cisiTermProb.items() if y != 0}
# cisiTermProb = dict(Counter(cisiTermProb).most_common(100))
#
# with open(cranTermProbFilePath, 'rb') as cran:
#     cranTermProb = pickle.load(cran)
# cranTermProb = {x: y for x, y in cranTermProb.items() if y != 0}
# cranTermProb = dict(Counter(cranTermProb).most_common(100))
#
# with open(medTermProbFilePath, 'rb') as med:
#     medTermProb = pickle.load(med)
# medTermProb = {x: y for x, y in medTermProb.items() if y != 0}
# medTermProb = dict(Counter(medTermProb).most_common(100))

with open(alt_atheismtermprobability, "rb") as alt_atheismtermprobabilityFile:
    alt_atheismtermprobabilityFileTermProb = pickle.load(alt_atheismtermprobabilityFile)
alt_atheismtermprobabilityFile = {x: y for x, y in alt_atheismtermprobabilityFileTermProb.items() if y != 0}
alt_atheismtermprobabilityFile = dict(Counter(alt_atheismtermprobabilityFileTermProb).most_common(100))
with open(comp_graphicstermprobability, "rb") as comp_graphicstermprobabilityFile:
    comp_graphicstermprobabilityFileTermProb = pickle.load(comp_graphicstermprobabilityFile)
comp_graphicstermprobabilityFile = {x: y for x, y in comp_graphicstermprobabilityFileTermProb.items() if y != 0}
comp_graphicstermprobabilityFile = dict(Counter(comp_graphicstermprobabilityFileTermProb).most_common(100))
with open(comp_os_ms_windows_misctermprobability, "rb") as comp_os_ms_windows_misctermprobabilityFile:
    comp_os_ms_windows_misctermprobabilityFileTermProb = pickle.load(comp_os_ms_windows_misctermprobabilityFile)
comp_os_ms_windows_misctermprobabilityFile = {x: y for x, y in comp_os_ms_windows_misctermprobabilityFileTermProb.items() if y != 0}
comp_os_ms_windows_misctermprobabilityFile = dict(Counter(comp_os_ms_windows_misctermprobabilityFileTermProb).most_common(100))
with open(comp_sys_ibm_pc_hardwaretermprobability, "rb") as comp_sys_ibm_pc_hardwaretermprobabilityFile:
    comp_sys_ibm_pc_hardwaretermprobabilityFileTermProb = pickle.load(comp_sys_ibm_pc_hardwaretermprobabilityFile)
comp_sys_ibm_pc_hardwaretermprobabilityFile = {x: y for x, y in comp_sys_ibm_pc_hardwaretermprobabilityFileTermProb.items() if y != 0}
comp_sys_ibm_pc_hardwaretermprobabilityFile = dict(Counter(comp_sys_ibm_pc_hardwaretermprobabilityFileTermProb).most_common(100))
with open(comp_sys_mac_hardwaretermprobability, "rb") as comp_sys_mac_hardwaretermprobabilityFile:
    comp_sys_mac_hardwaretermprobabilityFileTermProb = pickle.load(comp_sys_mac_hardwaretermprobabilityFile)
comp_sys_mac_hardwaretermprobabilityFile = {x: y for x, y in comp_sys_mac_hardwaretermprobabilityFileTermProb.items() if y != 0}
comp_sys_mac_hardwaretermprobabilityFile = dict(Counter(comp_sys_mac_hardwaretermprobabilityFileTermProb).most_common(100))
with open(comp_windows_xtermprobability, "rb") as comp_windows_xtermprobabilityFile:
    comp_windows_xtermprobabilityFileTermProb = pickle.load(comp_windows_xtermprobabilityFile)
comp_windows_xtermprobabilityFile = {x: y for x, y in comp_windows_xtermprobabilityFileTermProb.items() if y != 0}
comp_windows_xtermprobabilityFile = dict(Counter(comp_windows_xtermprobabilityFileTermProb).most_common(100))
with open(misc_forsaletermprobability, "rb") as misc_forsaletermprobabilityFile:
    misc_forsaletermprobabilityFileTermProb = pickle.load(misc_forsaletermprobabilityFile)
misc_forsaletermprobabilityFile = {x: y for x, y in misc_forsaletermprobabilityFileTermProb.items() if y != 0}
misc_forsaletermprobabilityFile = dict(Counter(misc_forsaletermprobabilityFileTermProb).most_common(100))
with open(rec_autostermprobability, "rb") as rec_autostermprobabilityFile:
    rec_autostermprobabilityFileTermProb = pickle.load(rec_autostermprobabilityFile)
rec_autostermprobabilityFile = {x: y for x, y in rec_autostermprobabilityFileTermProb.items() if y != 0}
rec_autostermprobabilityFile = dict(Counter(rec_autostermprobabilityFileTermProb).most_common(100))
with open(rec_motorcyclestermprobability, "rb") as rec_motorcyclestermprobabilityFile:
    rec_motorcyclestermprobabilityFileTermProb = pickle.load(rec_motorcyclestermprobabilityFile)
rec_motorcyclestermprobabilityFile = {x: y for x, y in rec_motorcyclestermprobabilityFileTermProb.items() if y != 0}
rec_motorcyclestermprobabilityFile = dict(Counter(rec_motorcyclestermprobabilityFileTermProb).most_common(100))
with open(rec_sport_baseballtermprobability, "rb") as rec_sport_baseballtermprobabilityFile:
    rec_sport_baseballtermprobabilityFileTermProb = pickle.load(rec_sport_baseballtermprobabilityFile)
rec_sport_baseballtermprobabilityFile = {x: y for x, y in rec_sport_baseballtermprobabilityFileTermProb.items() if y != 0}
rec_sport_baseballtermprobabilityFile = dict(Counter(rec_sport_baseballtermprobabilityFileTermProb).most_common(100))
with open(rec_sport_hockeytermprobability, "rb") as rec_sport_hockeytermprobabilityFile:
    rec_sport_hockeytermprobabilityFileTermProb = pickle.load(rec_sport_hockeytermprobabilityFile)
rec_sport_hockeytermprobabilityFile = {x: y for x, y in rec_sport_hockeytermprobabilityFileTermProb.items() if y != 0}
rec_sport_hockeytermprobabilityFile = dict(Counter(rec_sport_hockeytermprobabilityFileTermProb).most_common(100))
with open(sci_crypttermprobability, "rb") as sci_crypttermprobabilityFile:
    sci_crypttermprobabilityFileTermProb = pickle.load(sci_crypttermprobabilityFile)
sci_crypttermprobabilityFile = {x: y for x, y in sci_crypttermprobabilityFileTermProb.items() if y != 0}
sci_crypttermprobabilityFile = dict(Counter(sci_crypttermprobabilityFileTermProb).most_common(100))
with open(sci_electronicstermprobability, "rb") as sci_electronicstermprobabilityFile:
    sci_electronicstermprobabilityFileTermProb = pickle.load(sci_electronicstermprobabilityFile)
sci_electronicstermprobabilityFile = {x: y for x, y in sci_electronicstermprobabilityFileTermProb.items() if y != 0}
sci_electronicstermprobabilityFile = dict(Counter(sci_electronicstermprobabilityFileTermProb).most_common(100))
with open(sci_medtermprobability, "rb") as sci_medtermprobabilityFile:
    sci_medtermprobabilityFileTermProb = pickle.load(sci_medtermprobabilityFile)
sci_medtermprobabilityFile = {x: y for x, y in sci_medtermprobabilityFileTermProb.items() if y != 0}
sci_medtermprobabilityFile = dict(Counter(sci_medtermprobabilityFileTermProb).most_common(100))
with open(sci_spacetermprobability, "rb") as sci_spacetermprobabilityFile:
    sci_spacetermprobabilityFileTermProb = pickle.load(sci_spacetermprobabilityFile)
sci_spacetermprobabilityFile = {x: y for x, y in sci_spacetermprobabilityFileTermProb.items() if y != 0}
sci_spacetermprobabilityFile = dict(Counter(sci_spacetermprobabilityFileTermProb).most_common(100))
with open(soc_religion_christiantermprobability, "rb") as soc_religion_christiantermprobabilityFile:
    soc_religion_christiantermprobabilityFileTermProb = pickle.load(soc_religion_christiantermprobabilityFile)
soc_religion_christiantermprobabilityFile = {x: y for x, y in soc_religion_christiantermprobabilityFileTermProb.items() if y != 0}
soc_religion_christiantermprobabilityFile = dict(Counter(soc_religion_christiantermprobabilityFileTermProb).most_common(100))
with open(talk_politics_gunstermprobability, "rb") as talk_politics_gunstermprobabilityFile:
    talk_politics_gunstermprobabilityFileTermProb = pickle.load(talk_politics_gunstermprobabilityFile)
talk_politics_gunstermprobabilityFile = {x: y for x, y in talk_politics_gunstermprobabilityFileTermProb.items() if y != 0}
talk_politics_gunstermprobabilityFile = dict(Counter(talk_politics_gunstermprobabilityFileTermProb).most_common(100))
with open(talk_politics_mideasttermprobability, "rb") as talk_politics_mideasttermprobabilityFile:
    talk_politics_mideasttermprobabilityFileTermProb = pickle.load(talk_politics_mideasttermprobabilityFile)
talk_politics_mideasttermprobabilityFile = {x: y for x, y in talk_politics_mideasttermprobabilityFileTermProb.items() if y != 0}
talk_politics_mideasttermprobabilityFile = dict(Counter(talk_politics_mideasttermprobabilityFileTermProb).most_common(100))
with open(talk_politics_misctermprobability, "rb") as talk_politics_misctermprobabilityFile:
    talk_politics_misctermprobabilityFileTermProb = pickle.load(talk_politics_misctermprobabilityFile)
talk_politics_misctermprobabilityFile = {x: y for x, y in talk_politics_misctermprobabilityFileTermProb.items() if y != 0}
talk_politics_misctermprobabilityFile = dict(Counter(talk_politics_misctermprobabilityFileTermProb).most_common(100))
with open(talk_religion_misctermprobability, "rb") as talk_religion_misctermprobabilityFile:
    talk_religion_misctermprobabilityFileTermProb = pickle.load(talk_religion_misctermprobabilityFile)
talk_religion_misctermprobabilityFile = {x: y for x, y in talk_religion_misctermprobabilityFileTermProb.items() if y != 0}
talk_religion_misctermprobabilityFile = dict(Counter(talk_religion_misctermprobabilityFileTermProb).most_common(100))


for docType in docTypeList:
    print(docType)
    if docType != 'Testingtermfrequency':
        classPath = inputDirectory + '/' + docType
        files = os.listdir(classPath)
        #        outputDict={'File Name':{'cacm','cisi','cran','med','max','result class','result'}}
        outputCounterFilepath = outputDirectory + '/' + docType
        outputExcelFilepath = outputDirectory + '/' + docType + '.csv'
        outputExcelFilepathOne=outputDirectory + '/' + docType + 'ADDED.csv'
        outputDict = {}
        outputList = []
        for targetfile in files:
            if targetfile != 'classtermfrequency':
                # fileCacm = 0
                # fileCisi = 0
                # fileCran = 0
                # fileMed = 0
                filealt_atheismtermprobability = 0
                filecomp_graphicstermprobability = 0
                filecomp_os_ms_windows_misctermprobability = 0
                filecomp_sys_ibm_pc_hardwaretermprobability = 0
                filecomp_sys_mac_hardwaretermprobability = 0
                filecomp_windows_xtermprobability = 0
                filemisc_forsaletermprobability = 0
                filerec_autostermprobability = 0
                filerec_motorcyclestermprobability = 0
                filerec_sport_baseballtermprobability = 0
                filerec_sport_hockeytermprobability = 0
                filesci_crypttermprobability = 0
                filesci_electronicstermprobability = 0
                filesci_medtermprobability = 0
                filesci_spacetermprobability = 0
                filesoc_religion_christiantermprobability = 0
                filetalk_politics_gunstermprobability = 0
                filetalk_politics_mideasttermprobability = 0
                filetalk_politics_misctermprobability = 0
                filetalk_religion_misctermprobability = 0
                filePath = classPath + '/' + targetfile
                with open(filePath, 'rb') as fp:
                    fileTermList = pickle.load(fp)

                for fileTerm in fileTermList.keys():
                    if fileTerm in alt_atheismtermprobabilityFile:
                        filealt_atheismtermprobability = filealt_atheismtermprobability + \
                                                         alt_atheismtermprobabilityFile[fileTerm]
                    if fileTerm in comp_graphicstermprobabilityFile:
                        filecomp_graphicstermprobability = filecomp_graphicstermprobability + \
                                                           comp_graphicstermprobabilityFile[fileTerm]
                    if fileTerm in comp_os_ms_windows_misctermprobabilityFile:
                        filecomp_os_ms_windows_misctermprobability = filecomp_os_ms_windows_misctermprobability + comp_os_ms_windows_misctermprobabilityFile[fileTerm]
                    if fileTerm in comp_sys_ibm_pc_hardwaretermprobabilityFile:
                        filecomp_sys_ibm_pc_hardwaretermprobability = filecomp_sys_ibm_pc_hardwaretermprobability + \
                                                                      comp_sys_ibm_pc_hardwaretermprobabilityFile[
                                                                          fileTerm]
                    if fileTerm in comp_sys_mac_hardwaretermprobabilityFile:
                        filecomp_sys_mac_hardwaretermprobability = filecomp_sys_mac_hardwaretermprobability + \
                                                                   comp_sys_mac_hardwaretermprobabilityFile[fileTerm]
                    if fileTerm in comp_windows_xtermprobabilityFile:
                        filecomp_windows_xtermprobability = filecomp_windows_xtermprobability + \
                                                            comp_windows_xtermprobabilityFile[fileTerm]
                    if fileTerm in misc_forsaletermprobabilityFile:
                        filemisc_forsaletermprobability = filemisc_forsaletermprobability + \
                                                          misc_forsaletermprobabilityFile[fileTerm]
                    if fileTerm in rec_autostermprobabilityFile:
                        filerec_autostermprobability = filerec_autostermprobability + rec_autostermprobabilityFile[
                            fileTerm]
                    if fileTerm in rec_motorcyclestermprobabilityFile:
                        filerec_motorcyclestermprobability = filerec_motorcyclestermprobability + \
                                                             rec_motorcyclestermprobabilityFile[fileTerm]
                    if fileTerm in rec_sport_baseballtermprobabilityFile:
                        filerec_sport_baseballtermprobability = filerec_sport_baseballtermprobability + \
                                                                rec_sport_baseballtermprobabilityFile[fileTerm]
                    if fileTerm in rec_sport_hockeytermprobabilityFile:
                        filerec_sport_hockeytermprobability = filerec_sport_hockeytermprobability + \
                                                              rec_sport_hockeytermprobabilityFile[fileTerm]
                    if fileTerm in sci_crypttermprobabilityFile:
                        filesci_crypttermprobability = filesci_crypttermprobability + sci_crypttermprobabilityFile[
                            fileTerm]
                    if fileTerm in sci_electronicstermprobabilityFile:
                        filesci_electronicstermprobability = filesci_electronicstermprobability + \
                                                             sci_electronicstermprobabilityFile[fileTerm]
                    if fileTerm in sci_medtermprobabilityFile:
                        filesci_medtermprobability = filesci_medtermprobability + sci_medtermprobabilityFile[fileTerm]
                    if fileTerm in sci_spacetermprobabilityFile:
                        filesci_spacetermprobability = filesci_spacetermprobability + sci_spacetermprobabilityFile[
                            fileTerm]
                    if fileTerm in soc_religion_christiantermprobabilityFile:
                        filesoc_religion_christiantermprobability = filesoc_religion_christiantermprobability + \
                                                                    soc_religion_christiantermprobabilityFile[fileTerm]
                    if fileTerm in talk_politics_gunstermprobabilityFile:
                        filetalk_politics_gunstermprobability = filetalk_politics_gunstermprobability + \
                                                                talk_politics_gunstermprobabilityFile[fileTerm]
                    if fileTerm in talk_politics_mideasttermprobabilityFile:
                        filetalk_politics_mideasttermprobability = filetalk_politics_mideasttermprobability + \
                                                                   talk_politics_mideasttermprobabilityFile[fileTerm]
                    if fileTerm in talk_politics_misctermprobabilityFile:
                        filetalk_politics_misctermprobability = filetalk_politics_misctermprobability + \
                                                                talk_politics_misctermprobabilityFile[fileTerm]
                    if fileTerm in talk_religion_misctermprobabilityFile:
                        filetalk_religion_misctermprobability = filetalk_religion_misctermprobability + \
                                                                talk_religion_misctermprobabilityFile[fileTerm]
                #     if fileTerm in alt_atheismtermprobabilityFile:
                #         fileCacm = fileCacm + alt_atheismtermprobabilityFile[fileTerm]
                #     if fileTerm in cisiTermProb:
                #         fileCisi = fileCisi + cisiTermProb[fileTerm]
                #     if fileTerm in cranTermProb:
                #         fileCran = fileCran + cranTermProb[fileTerm]
                #     if fileTerm in medTermProb:
                #         fileMed = fileMed + medTermProb[fileTerm]


                maxArray = []
                maxValue = 0
                if filealt_atheismtermprobability != 0:
                    maxArray.append(filealt_atheismtermprobability)
                if filecomp_graphicstermprobability != 0:
                    maxArray.append(filecomp_graphicstermprobability)
                if filecomp_os_ms_windows_misctermprobability != 0:
                    maxArray.append(filecomp_os_ms_windows_misctermprobability)
                if filecomp_sys_ibm_pc_hardwaretermprobability != 0:
                    maxArray.append(filecomp_sys_ibm_pc_hardwaretermprobability)
                if filecomp_sys_mac_hardwaretermprobability != 0:
                    maxArray.append(filecomp_sys_mac_hardwaretermprobability)
                if filecomp_windows_xtermprobability != 0:
                    maxArray.append(filecomp_windows_xtermprobability)
                if filemisc_forsaletermprobability != 0:
                    maxArray.append(filemisc_forsaletermprobability)
                if filerec_autostermprobability != 0:
                    maxArray.append(filerec_autostermprobability)
                if filerec_motorcyclestermprobability != 0:
                    maxArray.append(filerec_motorcyclestermprobability)
                if filerec_sport_baseballtermprobability != 0:
                    maxArray.append(filerec_sport_baseballtermprobability)
                if filerec_sport_hockeytermprobability != 0:
                    maxArray.append(filerec_sport_hockeytermprobability)
                if filesci_crypttermprobability != 0:
                    maxArray.append(filesci_crypttermprobability)
                if filesci_electronicstermprobability != 0:
                    maxArray.append(filesci_electronicstermprobability)
                if filesci_medtermprobability != 0:
                    maxArray.append(filesci_medtermprobability)
                if filesci_spacetermprobability != 0:
                    maxArray.append(filesci_spacetermprobability)
                if filesoc_religion_christiantermprobability != 0:
                    maxArray.append(filesoc_religion_christiantermprobability)
                if filetalk_politics_gunstermprobability != 0:
                    maxArray.append(filetalk_politics_gunstermprobability)
                if filetalk_politics_mideasttermprobability != 0:
                    maxArray.append(filetalk_politics_mideasttermprobability)
                if filetalk_politics_misctermprobability != 0:
                    maxArray.append(filetalk_politics_misctermprobability)
                if filetalk_religion_misctermprobability != 0:
                    maxArray.append(filetalk_religion_misctermprobability)
                # if fileCacm != 0:
                #     maxArray.append(fileCacm)
                # if fileCisi != 0:
                #     maxArray.append(fileCisi)
                # if fileCran != 0:
                #     maxArray.append(fileCran)
                # if fileCacm != 0:
                #     maxArray.append(fileCacm)
                # if fileMed != 0:
                #     maxArray.append(fileMed)

                if len(maxArray) != 0:
                    maxValue = max(maxArray)
                    if maxValue == filealt_atheismtermprobability:
                        outputClass = 'alt.atheism'
                    elif maxValue == filecomp_graphicstermprobability:
                        outputClass = 'comp.graphics'
                    elif maxValue == filecomp_os_ms_windows_misctermprobability:
                        outputClass = 'comp.os.ms-windows.misc'
                    elif maxValue == filecomp_sys_ibm_pc_hardwaretermprobability:
                        outputClass = 'comp.sys.ibm.pc.hardware'
                    elif maxValue == filecomp_sys_mac_hardwaretermprobability:
                        outputClass = 'comp.sys.mac.hardware'
                    elif maxValue == filecomp_windows_xtermprobability:
                        outputClass = 'comp.windows.x'
                    elif maxValue == filemisc_forsaletermprobability:
                        outputClass = 'misc.forsale'
                    elif maxValue == filerec_autostermprobability:
                        outputClass = 'rec.autos'
                    elif maxValue == filerec_motorcyclestermprobability:
                        outputClass = 'rec.motorcycles'
                    elif maxValue == filerec_sport_baseballtermprobability:
                        outputClass = 'rec.sport.baseball'
                    elif maxValue == filerec_sport_hockeytermprobability:
                        outputClass = 'rec.sport.hockey'
                    elif maxValue == filesci_crypttermprobability:
                        outputClass = 'sci.crypt'
                    elif maxValue == filesci_electronicstermprobability:
                        outputClass = 'sci.electronics'
                    elif maxValue == filesci_medtermprobability:
                        outputClass = 'sci.med'
                    elif maxValue == filesci_spacetermprobability:
                        outputClass = 'sci.space'
                    elif maxValue == filesoc_religion_christiantermprobability:
                        outputClass = 'soc.religion.christian'
                    elif maxValue == filetalk_politics_gunstermprobability:
                        outputClass = 'talk.politics.guns'
                    elif maxValue == filetalk_politics_mideasttermprobability:
                        outputClass = 'talk.politics.mideast'
                    elif maxValue == filetalk_politics_misctermprobability:
                        outputClass = 'talk.politics.misc'
                    elif maxValue == filetalk_religion_misctermprobability:
                        outputClass = 'talk.religion.misc'
                    # if maxValue == fileCacm:
                    #     outputClass = 'cacm'
                    # elif maxValue == fileCisi:
                    #     outputClass = 'cisi'
                    # elif maxValue == fileCran:
                    #     outputClass = 'cran'
                    # elif maxValue == fileMed:
                    #     outputClass = 'med'
                    if outputClass == docType:
                        outputValue = True
                    else:
                        outputValue = False
                else:
                    outputClass = 'undifined'
                    outputValue = 'undifined'
                outputDict.update({targetfile: {'alt.atheism':filealt_atheismtermprobability,'comp.graphics':filecomp_graphicstermprobability,
                                                'comp.os.ms-windows.misc':filecomp_os_ms_windows_misctermprobability,
                                                'comp.sys.ibm.pc.hardware':filecomp_sys_ibm_pc_hardwaretermprobability,
                                                'comp.sys.mac.hardware':filecomp_sys_mac_hardwaretermprobability,
                                                'comp.windows.x':filecomp_windows_xtermprobability,
                                                'misc.forsale':filemisc_forsaletermprobability,'rec.autos':filerec_autostermprobability,
                                                'rec.motorcycles':filerec_motorcyclestermprobability,
                                                'rec.sport.baseball':filerec_sport_baseballtermprobability,
                                                'rec.sport.hockey':filerec_sport_hockeytermprobability,
                                                'sci.crypt':filesci_crypttermprobability,'sci.electronics':filesci_electronicstermprobability,
                                                'sci.med':filesci_medtermprobability,'sci.space':filesci_spacetermprobability,
                                                'soc.religion.christian':filesoc_religion_christiantermprobability,
                                                'talk.politics.guns':filetalk_politics_gunstermprobability,
                                                'talk.politics.mideast':filetalk_politics_mideasttermprobability,
                                                'talk.politics.misc':filetalk_politics_misctermprobability,
                                                'talk.religion.misc':filetalk_religion_misctermprobability,

                                                'maxValue': maxValue, 'result class': outputClass,
                                                'result': outputValue}})
                outputList.append((filealt_atheismtermprobability,filecomp_graphicstermprobability,filecomp_os_ms_windows_misctermprobability,
                                   filecomp_sys_ibm_pc_hardwaretermprobability,filecomp_sys_mac_hardwaretermprobability,filecomp_windows_xtermprobability,
                                   filemisc_forsaletermprobability,filerec_autostermprobability,filerec_motorcyclestermprobability,
                                   filerec_sport_baseballtermprobability,filerec_sport_hockeytermprobability,filesci_crypttermprobability,
                                   filesci_electronicstermprobability,filesci_medtermprobability,filesci_spacetermprobability,
                                   filesoc_religion_christiantermprobability,filetalk_politics_gunstermprobability,
                                   filetalk_politics_mideasttermprobability,filetalk_politics_misctermprobability,filetalk_religion_misctermprobability,
                                    maxValue, outputClass, outputValue))
        with open(outputCounterFilepath, 'wb') as fp:
            pickle.dump(outputDict, fp)
        # with open(outputExcelFilepath, 'w') as exf:
        #     wr = csv.writer(exf, dialect='excel')
        #     wr.writerows(outputList)

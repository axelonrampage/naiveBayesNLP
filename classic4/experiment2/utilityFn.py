import os
inputDir='../../dataset/classic4/classProbability/counterforth/'
# print(os.listdir(inputDir))
filesList=os.listdir(inputDir)
for ad in filesList:
    address=inputDir+ad
    var=ad.replace('.','_')
    fullAddr=var+"='"+address+"'"
    # print(fullAddr)
    # print('Var',(var))
    # print('with open(',var,", "'"rb"'") as ",var+'File: \n    ',var+'FileTermProb=pickle.load(',var+'File)\n'
    #                         ,var+'File={x:y for x,y in ',var+'FileTermProb.items() if y!=0}\n'
    #       , var + 'File=dict(Counter(',var+'FileTermProb).most_common(1000))' )
    # print("if fileTerm in",var+'File:\n'
    #                            '    file'+var,'=file'+var+'+',var+'File[fileTerm]' )
    # print('file'+var+'=0')
    # print('if file'+var+'!=0:\n     maxArray.append(file'+var+')')
    lens=len(ad)-15
    foldStr=ad[:lens]
    print("'"+foldStr+"'",end=',')
    # print("elif  maxValue==file"+var+":\n   outputClass='"+foldStr+"'")
    # print("'"+foldStr+"'"+':file'+var,end=',')
    # print('file'+var,end=',')



# elif maxValue == fileCisi:
# outputClass = 'cisi'
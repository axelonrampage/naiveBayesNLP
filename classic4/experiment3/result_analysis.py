import numpy as np
import json
import result_function as rf
mostCommon=100
# result_array= [[8,2,0],[1,7,2],[0,1,9]]
# with open("result","w") as f:
#     f.write(json.dumps(result_array))
resultDir = '../../../dataset/classic4/experiment3/result/' + str(mostCommon) + 'Features/result'

with open(resultDir, "r") as f:
    file_array = json.loads(f.read())

result_array = np.array(file_array)
row_length, colomn_length = np.shape(result_array)
print('Row', row_length)
print("Column", colomn_length)
array_sum = np.sum(result_array)
row_sum = np.sum(result_array, axis=1)
col_sum = np.sum(result_array, axis=0)
result = []
print(result_array)
accuracyVar = 0
preciseVar = 0
for i in range(row_length):
    TP = 0
    TN = 0
    FP = 0
    FN = 0

    TP = result_array[i][i]
    FN = row_sum[i] - TP
    FP = col_sum[i] - TP
    TN = array_sum - row_sum[i] - col_sum[i] + TP
    precision = rf.precision(TP, FP)
    recall = rf.recall(TP, FN)
    accuracy = rf.accuracy(TP, TN, FP, FN)
    f1_score = rf.fscore(precision, recall)
    f0_5_score = rf.fscore(precision, recall, 0.5)
    f2_score = rf.fscore(precision, recall, 2)
    result.append([TP, TN, FP, FN, precision, recall, accuracy, f1_score])
    result[i] = [TP, TN, FP, FN, precision, recall, accuracy, f1_score]

    accuracyVar = accuracy + accuracyVar
    preciseVar = preciseVar + precision
    # print('True Positive',TP)
    # print('True Negative',TN)
    # print('False Positive',FP)
    # print('False Negative',FN)
    # print('Precision',precision)
    # print('Recall',recall)
    print('Accuracy', accuracy)
    # print('F0.5 Score',f0_5_score,end='\n')
    # print('F1 Score',f1_score,end='\n')
    # print('F2 Score',f2_score,end='\n')
# print(result)

print("\nAccuracyAverage", accuracyVar / 4)

with open(resultDir + "analysis", "w") as f:
    f.write(json.dumps(result, cls=rf.NpEncoder))



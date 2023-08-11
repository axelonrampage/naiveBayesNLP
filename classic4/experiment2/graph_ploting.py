import json
import numpy as np
import matplotlib.pyplot as plt

with open("result_analysis","r") as f:
    file_array = json.loads(f.read())
    
result_array = np.array(file_array)



TP=result_array[:,0]
TN=result_array[:,1]
FP=result_array[:,2]
FN=result_array[:,3]
precision=result_array[:,4]
recall=result_array[:,5]
accuracy=result_array[:,6]
f1_score=result_array[:,7]

class_x_axis=np.array([1,2,3,4])

print("Precision",precision)

print(recall)

print(accuracy)
print(f1_score)
# TP=result_array[:,0].tolist()
# TN=result_array[:,1].tolist()
# FP=result_array[:,2].tolist()
# FN=result_array[:,3].tolist()
# precision=result_array[:,4].tolist()
# recall=result_array[:,5].tolist()
# accuracy=result_array[:,6].tolist()
# f1_score=result_array[:,7].tolist()

# class_x_axis=[1,2,3]


plt.title("Result analysis") 
plt.xlabel("Classes") 
plt.ylabel("Value of different measures") 

plt.plot(class_x_axis, precision, label = "Precision")
plt.plot(class_x_axis, recall, label = "Recall")
plt.plot(class_x_axis, accuracy, label = "Accuracy")
# plt.plot(class_x_axis, f1_score,'--', label = "F1 Score")

plt.legend()
plt.show()

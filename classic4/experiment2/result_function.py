import json
import numpy as np


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            return super(NpEncoder, self).default(obj)
        

def precision(TP,FP):
    precision =  float(TP/(TP+FP))
    return precision

def recall(TP,FN):
    recall =  float(TP/(TP+FN))
    return recall

def accuracy(TP,TN,FP,FN):
    accuracy =  float((TP+TN)/(TP+TN+FP+FN))
    return accuracy

def fscore(precision,recall,beta=1):
    fscore=float((1+beta**2)*((precision*recall)/((beta**2)*precision+recall)))
    return fscore
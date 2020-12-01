import os
import sys
import os
import sys
import csv
import numpy as npy
import pandas as pd
from statistics import mean
from scipy.stats import entropy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,classification_report
from sklearn.svm import SVC
import matplotlib.pyplot as plt



def entropyVal(labels, base=None):
    value,counts = npy.unique(labels, return_counts=True)
    return entropy(counts, base=base)

def result(path):
    output=[]

    columnnames = ['subject','pain/nopain', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40']
    for subjects in os.scandir(path):

        for task in os.scandir(subjects.path):
            fileData=[]
            task_id=task.name

            if task_id=='T8':
                task_id=1
            else:
                task_id=0
            subject_id=subjects.name
            fileData.append(subject_id)
            fileData.append(task_id)

            for fileNames in os.scandir(task):
                if fileNames.name!='.DS_Store':
                    readFile = open(fileNames.path, "r")
                    fileLines = readFile.readlines()
                    loaddata = npy.array(fileLines).astype(float)
                    Mean=npy.mean(loaddata)
                    Maximum=max(loaddata)
                    Minimum=min(loaddata)
                    Variance=float("%3.4f" % (npy.var(loaddata)))
                    Entropy=float("%3.4f" % (entropyVal(loaddata)))
                    fileData.append(Mean)
                    fileData.append(Maximum)
                    fileData.append(Minimum)
                    fileData.append(Variance)
                    fileData.append(Entropy)
            output.append(fileData)

    out_dataframe = pd.DataFrame(output)
    out_dataframe.to_csv('output.csv')

def Svm(path):
    result(path)
    filePath='/home/CAP5627-5/output.csv'
    dataset=pd.read_csv(filePath)
    X = dataset.iloc[:, 3:43].values
    y = dataset.iloc[:,2].values
    train_x,test_x, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=0)
    clf = SVC(kernel='linear')
    clf.fit(train_x, train_y)
    v = clf.predict(test_x)
    print(confusion_matrix(test_y,v.round()))
    print(classification_report(test_y,v.round()))
    print(accuracy_score(test_y, v.round()))


def main():
    path = sys.argv[2]
    algorithm = sys.argv[1]
    #if algorithm == 'Svm':
    Svm(path)
main()

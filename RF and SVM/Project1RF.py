import os
import sys
import os
import sys
import csv
import numpy as np
import pandas as pd
from statistics import mean
from scipy.stats import entropy
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix,classification_report

def result(datapath,algorithm):
    
    result_value=[]
    
    for subjects in os.listdir(datapath):
        subject_path=os.path.join(datapath,subjects)
        for tasks in os.listdir(subject_path):
            mean=[]
            maxi=[]
            mini=[]
            var=[]
            ent=[]
            subject_list=[]
            task_list=[]
            subject_list.append(subjects)
            task_path=os.path.join(subject_path,tasks)
            if tasks=='T8':
                tasks='1'
            else:
                tasks='0'
            task_list.append(tasks)
            for files in os.listdir(task_path):
                if files != '.DS_Store' and files != 'ECG_mV.txt':                       
                    file_path=os.path.join(task_path,files)
                    data=np.loadtxt(file_path, dtype='float')
                    Mean=np.mean(data)
                    mean.append(Mean)
                    Variance=np.var(data)
                    var.append(Variance)
                    Minimum=min(data)
                    mini.append(Minimum)
                    Maximum=max(data)
                    maxi.append(Maximum)
                    Entropy=max(data)
                    ent.append(Entropy)
                    output=mean+var+mini+maxi+ent      
            result_name=subject_list+task_list+output     
            result_value.append(result_name)
        
    with open('results.csv', 'w') as myfile:
        wr = csv.writer(myfile, lineterminator='\n')
        wr.writerows(result_value)
    if algorithm=='RF':
        randomForest()
    else:
        svm() 
        
def split_dataset(dataset, train_percentage, feature_headers, target_header):
 
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers], dataset[target_header],
                                                        train_size=train_percentage)
    return train_x, test_x, train_y, test_y
    
        
def randomForest():
    filePath='/home/CAP5627-5/results.csv'
    dataset=pd.read_csv(filePath, header=None) 
   # for row in dataset:
    #    row[1]=float(row[1].strip())
    X = dataset.iloc[:, 2:42].values  
    Y = dataset.iloc[:, 1].values 
    train_x, test_x, train_y, test_y = train_test_split(X, Y, train_size=0.8)
    #train_x, test_x, train_y, test_y = split_dataset(dataset, 0.8, dataset[2:], dataset[1])
    clf = RandomForestClassifier()
    trained_model=clf.fit(train_x, train_y)
    rnc =RandomForestClassifier(random_state=4,n_estimators=20,n_jobs=10)
    rnc.fit(train_x,train_y)
    y_pred=rnc.predict(test_x)
    print ("Trained model :: ", trained_model)
    predictions = trained_model.predict(test_x)
    print ("Train Accuracy :: ", accuracy_score(train_y, trained_model.predict(train_x)))
    print ("Test Accuracy  :: ", accuracy_score(test_y, predictions))
    print ("Confusion matrix ", confusion_matrix(test_y, predictions))
    print(classification_report(test_y,y_pred))  
    


    
def main():
    dataset = sys.argv[2]
    algorithm = sys.argv[1]
    if dataset=='Dataset1':
        datapath='/home/CAP5627-5/affective/Dataset1/'
    else:
        datapath='/home/CAP5627-5/affective/Dataset2/'
    result(datapath,algorithm)
    

main()   
    
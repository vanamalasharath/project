import math
import os
import sys
import random
import numpy as np
import matplotlib.pyplot as plt

def locations_read():
    x_cord=[]
    y_cord=[]
    name1=[]
    colors=(0,0,0)
    locations_file="locations.txt"
    if not os.path.isfile(locations_file):
        print("Locations file is missing")
        sys.exit()
    file = open(locations_file,"r")
    for i in file:
        
        records=i.split()
        loc=records[0]
        if loc!='END' :
            #print(records)
            #print(loc)
            one=int(records[1])
            two=int(records[2])
            name=records[0]
            x_cord.append(one)
            y_cord.append(two)
            name1.append(name)
    #print(x_cord)
    #print(y_cord)
    #colors =(0,0,0)
            plt.scatter(one, two, c=colors, alpha=0.5)
            plt.text(one+0.3,two+0.3,name, fontsize=9)
    plt.title('scatter plot')
    plt.show()


locations_read()
        

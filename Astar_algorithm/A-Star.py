import math
import os
import sys
import random
import numpy as np
import matplotlib.pyplot as plt
def locations_read():
    locations_file="locations.txt"
    records=[]
    if not os.path.isfile(locations_file):
        print("Locations file is missing")
        sys.exit()
    loc_dict={}
    with open(locations_file,"r") as file:
        for i in file:
            records=i.split()
            if records[0]!="END":
                key=records[0]
                values=[records[1],records[2]]
                loc_dict[key]=values
    return loc_dict
        
def connections_read():
    connections_file="connections.txt"
    records=[]
    if not os.path.isfile(connections_file):
        print("connections file is missing")
        sys.exit()
    conn_dict = {}
    with open(connections_file,"r") as file:
        for i in file:
            records = i.split()
            if records[0]!="END":
                key = records[0]
                values = records[2:]
                conn_dict[key]=values
    return conn_dict
        
def distance_calculation(src,des,loc_dict,heuristic):
    if heuristic==2:
        return 1
    else:        
        x1=int(loc_dict[src][0])
        y1=int(loc_dict[src][1])
        x2=int(loc_dict[des][0])
        y2=int(loc_dict[des][1])
        distance=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
        return distance

def current_to_end_distance(conn_dict,destination,loc_dict,heuristic):
    current_to_end={}
    if destination in conn_dict.keys():
        for i in conn_dict.keys():     
            current_to_end[i]=distance_calculation(i,destination,loc_dict,heuristic)
        return current_to_end
    else:
        print("Enter a valid end city")
def graph_plot(loc_dict,path,explored_nodes):
    
    x_cord=[]
    y_cord=[]
    name1=[]
    x22=[]
    y22=[]
    x33=[]
    y33=[]
    #path=['A1','A2','B1']
    colors=(0,0,0)
    connections="connections.txt"
    locations_file="locations.txt"
    for i in loc_dict.keys():
        one=int(loc_dict[i][0])
        two=int(loc_dict[i][1])
        name=i
        x_cord.append(one)
        y_cord.append(two)
        name1.append(name)
        type(one)
        plt.scatter(one, two, c=colors, alpha=0.5)
        plt.text(one+0.3,two+0.3,name, fontsize=9)
    plt.title('Cities plot')
    file1 = open(connections,"r")
    file2 = open(locations_file,"r")
    for i in file1:
        n1=i.split()
        if n1[0] != 'END':
            a1=n1[0]
            b1=int(n1[1])
            temp=int(n1[1])
            i=2
            for j in range(b1) :
                var=n1[i]
                file2 = open(locations_file,"r")
                x11=[]
                y11=[]
                for k in file2:
                    new=k.split()
                    if a1==new[0]:
                        a=float(new[1])
                        b=float(new[2])
                        x11.append(a)
                        y11.append(b)
                    if var==new[0]:
                        a=float(new[1])
                        b=float(new[2])
                        x11.append(a)
                        y11.append(b)
                i=i+1
                plt.plot(x11,y11,linewidth=1,color='black')
    
                
    for j in path:
        file = open(locations_file,"r")
        for i in file:
            new=i.split()
            if j==new[0]:
                a=float(new[1])
                b=float(new[2])
                x22.append(a)
                y22.append(b)
    plt.plot(x22,y22,linewidth=3,color='red')
    for j in explored_nodes:
        file = open(locations_file,"r")
        for i in file:
            new=i.split()
            if j==new[0]:
                a=float(new[1])
                b=float(new[2])
                x33.append(a)
                y33.append(b)
    #print(x11)
    plt.plot(x33,y33,'--',linewidth=1,color='yellow')
    plt.show()
         
     
def heuristic_Astar(source,destination,exclusions,path_way,conn_dict,loc_dict,current_to_end,heuristic):
    print("----------------*----------------")
    if heuristic==1:
        print("straight line distance heuristic")
    else:
        print("Fewest cities heuristic")
    print("----------------*----------------")       
    open_nodes=[]
    explored_nodes=[]
    optimal_path_nodes={}
    total_distance=0
    start_to_now={}
    total_cost={}
    start_to_now[source]=0
    total_cost[source]=0
    distance_covered=0
    if source==destination:
        final_path=[source]
        explored_nodes=[source]
        print("start city and end city are same")
        print("Total path length : ",total_distance)
        return final_path,explored_nodes
    open_nodes.append(source)
    while open_nodes:
        min_dict={}
        for key,value in total_cost.items():
            if key in open_nodes:
                min_dict[key]=value
        new_source=min(min_dict.keys(), key=(lambda k: min_dict[k]))
        explored_nodes.append(new_source)            
        open_nodes.remove(new_source)
        if new_source==destination:
            final_path=[]
            print("........................................................................")
            print("The final solution path is : ")
            print("........................................................................")
            final_path.append(destination)
            while destination in optimal_path_nodes.keys():
                destination=optimal_path_nodes[destination]
                final_path.insert(0,destination)
            for k in range (len(final_path)-1):
                src=final_path[k]
                des=final_path[k+1]
                distance_covered=distance_calculation(src,des,loc_dict,heuristic)
                print(src," to ", des," length ",distance_covered)
                total_distance=distance_covered+total_distance
            print("........................................................................")
            print("Total path length: ",total_distance)
            print("........................................................................")
            return final_path,explored_nodes
        connections=conn_dict[new_source]
        if path_way==1:
            print("City selected: ", new_source)
            print("Possible cities to travel: ",connections)
        if len(connections)>0:            
            for j in connections:
                if j not in explored_nodes:
                    source_to_child_dist=distance_calculation(new_source,j,loc_dict,heuristic)
                    new_distance=source_to_child_dist+start_to_now[new_source]
                    result=j in start_to_now.keys()
                    if result==True:
                        if new_distance<start_to_now[j]:
                            if j not in open_nodes:
                                open_nodes.append(j)
                            start_to_now[j]=new_distance
                            total_cost[j]=start_to_now[j]+current_to_end[j]
                            optimal_path_nodes[j]=new_source
                    else:
                        if j not in open_nodes:
                            open_nodes.append(j)
                        start_to_now[j]=new_distance
                        total_cost[j]=start_to_now[j]+current_to_end[j]
                        optimal_path_nodes[j]=new_source
        else:
            print("No connections exist")
        if path_way==1:
            if len(open_nodes)!=0:
                print("Cities at the end of possible paths: ")
                for k in open_nodes:
                    print(k,"(",total_cost[k],") ")
                print("************************************************************************")
        
    if len(open_nodes) == 0:
        print("No path exists")
        

    
def main():
    # input
    conn_dict=connections_read()
    all_keys=list(conn_dict.keys())
    loc_dict=locations_read()
    exclusions=[]
    total_distance=0
    print("******Welcome to A Star Algorithm********")
    
    while True:
        try:
            source=str(input("Enter start city: "))
            destination=str(input("Enter end city: "))
            exclusions=str(input("Enter city name(s) that should not be included in the solution path : ")).split()
            X=all(i in all_keys  for i in exclusions)
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if source not in all_keys:
            print("Enter Valid start city.")
            continue
       
        elif destination not in all_keys:
            print("Enter Valid end city.")
            continue
        
        elif source in exclusions:
            print("start city cannot be included  in exclusions")
            continue
        elif destination in exclusions:
            print("end city cannot be included in exclusions")
            continue
        elif X is False :
            print("Enter Valid city name(s) that should not be included in the solution path.")
            continue
       
        else:
            break

    path_way=int(input("Enter 1 for step by step procedure or enter 2 to view only optimal path :"))
    heuristic=int(input("Enter 1 for straight line distance heuristic and 2 for fewest cities heuristic :"))
    for i in exclusions:
        if i in conn_dict:
            del conn_dict[i]
        for v in conn_dict.values():
            for j in v:
                if i==j:
                    v.remove(j)
    current_to_end=current_to_end_distance(conn_dict,destination,loc_dict,heuristic)
    if heuristic == 1:
        final_path,explored_nodes=heuristic_Astar(source,destination,exclusions,path_way,conn_dict,loc_dict,current_to_end,heuristic)
    elif heuristic == 2:
        final_path,explored_nodes=heuristic_Astar(source,destination,exclusions,path_way,conn_dict,loc_dict,current_to_end,heuristic)
    #print(explored_nodes)
    if len(explored_nodes)>1:
        graph_plot(loc_dict,final_path,explored_nodes)
    else:
        print("Start and end city are same. so no path exists")

    
main()
    
    

import csv
import sys
import math
from math import radians, cos, sin, asin, sqrt

def read_csv_file(filename):
    data=[]
    with open(filename,'r') as file:
        csv_reader=csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calculate_distance(alt1, lat1, lon1, alt2, lat2, lon2):
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    x1 = alt1 * math.cos(lat1_rad) * math.cos(lon1_rad)
    y1 = alt1 * math.cos(lat1_rad) * math.sin(lon1_rad)
    z1 = alt1 * math.sin(lat1_rad)

    x2 = alt2 * math.cos(lat2_rad) * math.cos(lon2_rad)
    y2 = alt2 * math.cos(lat2_rad) * math.sin(lon2_rad)
    z2 = alt2 * math.sin(lat2_rad)

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance

csv_filename='Computer-network/Dataset.csv'
ls=read_csv_file(csv_filename)

LHR=[81.73,0.4543,51.4700]
EWR=[8.72,74.1745,40.6895]
x=sys.maxsize
i=0
j=0
ls3=[]

def iterations(ls2,g):
    for q in range(2,5):
        ls2.append(ls[g][q])
    return ls2

def calculate_delay(a,b,c,d,e,f):
    a_rad = math.radians(a)
    b_rad = math.radians(b)
    delay1 = math.sin(a_rad)+math.cos(b_rad)+c
    d_rad = math.radians(d)
    e_rad = math.radians(e)
    delay2 = math.sin(d_rad)+math.cos(e_rad)+f
    
    totaldelay = delay1+delay2



    return totaldelay
ls4=[]
routpath=[]


while(j<149):
    n=j+1
    ls1=ls[i][2:5]
    a=float(ls1[0])
    b=float(ls1[1])
    c=float(ls1[2])
    l=0
    for k in range(n,149):
        ls2=ls[n][2:5]
        d=float(ls2[0])
        e=float(ls2[1])
        f=float(ls2[2])
        a1=calculate_delay(a,b,c,d,e,f)
        a2=calculate_delay(a,b,c,LHR[0],LHR[1],LHR[2])
        a3=calculate_delay(a,b,c,EWR[0],EWR[1],EWR[2])
        a4=calculate_delay(d,e,f,LHR[0],LHR[1],LHR[2])
        a5=calculate_delay(d,e,f,EWR[0],EWR[1],EWR[2])
        d1=a1+a2
        d2=a1+a3
        d3=a1+a4
        d4=a1+a5
        j1=min(d1,d2,d3,d4)
        if(j1<x):
            if(j1==d1  or j1==d3):
                routpath.append([n,j,'LHR'])
            elif(j1==d2 or j1==d4):
                routpath.append([n,j,'EWR'])







            ls4.append(j1)
            x=j1

        

    x=sys.maxsize        
    j+=1


while(i<149):
    n=i+1
    ls1 = ls[i][2:5]
    # for j in range(2,5):
    #   ls1.append(ls[i][j])
    a=float(ls1[0])
    b=float(ls1[1])
    c=float(ls1[2]) 
    
    for k in range(n,149):
        ls2 = ls[n][2:5]
        d=float(ls2[0])
        e=float(ls2[1])
        f=float(ls2[2])
        a1=calculate_distance(a,b,c,d,e,f)
        a2=calculate_distance(a,b,c,LHR[0],LHR[1],LHR[2])
        a3=calculate_distance(a,b,c,EWR[0],EWR[1],EWR[2])
        a4=calculate_distance(d,e,f,LHR[0],LHR[1],LHR[2])
        a5=calculate_distance(d,e,f,EWR[0],EWR[1],EWR[2])
  

        k=min(a1,a2,a3,a4,a5)
        if(k<x):
            ls3.append(k)
            x=k

            
    x=sys.maxsize        
    i+=1
minimum_data_latency=min(ls4)
maximum_transmission_data=max(ls3)
print(routpath)

print(ls4.index(minimum_data_latency))
print(ls3.index(maximum_transmission_data))
print(len(routpath))
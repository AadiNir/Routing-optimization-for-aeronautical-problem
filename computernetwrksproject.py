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

csv_filename='Dataset.csv'
ls=read_csv_file(csv_filename)

LHR=[81.73,0.4543,51.4700]
EWR=[8.72,74.1745,40.6895]
x=sys.maxsize
i=0
ls3=[]

def iterations(ls2,g):
    for q in range(2,5):
        ls2.append(ls[g][q])
    return ls2


while(i<149):
    n=i+1
    ls1 = ls[i][2:5]
    # for j in range(2,5):
    #   ls1.append(ls[i][j])
    a=float(ls1[0])
    b=float(ls1[1])
    c=float(ls1[2]) 
    
    for k in range(n,149):
        # ls2=iterations(ls1,a)
        ls2 = ls[n][2:5]
        # print(ls2)
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

print(len(ls3))
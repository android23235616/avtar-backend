# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 14:37:23 2018

@author: Tanmay
"""



import pandas as pd

import geopy


import time
import numpy as np

import os




directory = './'

file_name = 'data2.csv'

path = os.path.join(directory,file_name)

df = pd.read_csv(path)

asd = df['area']

rapes = df['NUM']


def get_letter(times):
    times = int(times)
    if(times>=0 and times<=6):
        return 'MN'
    elif(times>=7 and times<11):
        return "M"
    elif(times>=12 and times<=19):
        return "E"
    elif(times>=19 and times<=23):
        return "N"


times = {'M':1,'N':2,"E":3,"MN":4}


def normalize(x,sets):





    temp = np.array(sets)
    x_new = (x - min(temp))/(max(temp)-min(temp))
    x_new = round(x_new,2)
    return (x_new)


area_index = {}

for i in range(len(asd)):
    area_index[asd[i]] = len(area_index)
    i+=30


x_data = []
y = []
def get_number(city, time):
    a1 = city

    b1 = time

    for area,time,r in zip(df['area'],df['Y'],df['NUM']):
        a = [area_index[area],times[time]]
       # b = normalize(r)
        #x_data.append(a)
        #y.append([b])
        if(a1==a[0] and b1==a[1]):
            x_data.append(r)

    #for i in x_data:
    #    a = normalize(i,x_data)
    #    normalized.append(a)
    #
    #means = np.array(normalized).mean()

    a = normalize(np.mean(x_data),x_data)

    a = round(a,2)
    return str(5-5*a)




geolocator =geopy.geocoders.GoogleV3()
def take_data(lat,lng,entryTime=time.strftime("%H")):



    location = geolocator.reverse(lat+","+lng)

    address = location[0]

    s = str(address)

    temp = "Odisha"

    for a in s.split(","):
        for b in a.split():
            if(len(b)>=6 and b.isdigit()):
                temp = a[1:len(a)-1-6]
                temp= temp.rstrip()




#    return str(address)

    #address = re.findall(r'_(\d{6})',str( address))


    print(len(temp))

    a1 = area_index[temp]
    b1 = times[get_letter(entryTime)]



    return get_number(a1,b1)














# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:25:02 2018

@author: Tanmay
"""

class location:
    def __init__(self, timeStamp, lat, lng):
        self.timeStamp = timeStamp
        self.lat = lat
        self.lng = lng


    def getTimeStamp(self):
        return self.timeStamp
    def getLat(self):
        return self.lat
    def getLng(self):
        return self.lng
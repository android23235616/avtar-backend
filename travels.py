# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:11:46 2018

@author: Tanmay
"""

class Travels:
    def __init__(self, chesis, locationStart=None, locationStop=None):
        self.chesis = chesis
        self.locationStart = locationStart
        self.locationStop = locationStop


    def get_chesis(self):
        return self.chesis

    def get_timeStart(self):
        return self.locationStart

    def get_timeStop(self):
        return self.locationStop

    def set_timeStart(self,location):
        self.locationStart = location

    def set_timeStop(self,location):
        self.locationStop = location


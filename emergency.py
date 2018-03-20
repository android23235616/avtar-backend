# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 01:01:02 2018

@author: Tanmay
"""
import time
class Emergency:
    def __init__(self,victim, vehicle):
        self.stamp = time.strftime("%c")
        self.victim = victim
        self.vehicle = vehicle
        self.id = victim.get_ssos()+"_"+str(time.time())

    def get_victim(self):
        return self.victim
    def get_vehicle(self):
        return self.vehicle
    def get_time(self):
        return self.stamp
    def get_passenger_ssos(self):
        p = self.victim
        return p.get_ssos()
    def get_id(self):
        return self.id
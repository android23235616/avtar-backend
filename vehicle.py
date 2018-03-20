# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 00:04:12 2018

@author: Tanmay
"""

class Vehicle:



    def __init__(self,chasis,ap,owner=None, plate=None):

        self.chasis_number = chasis
        self.ap_mac = ap
        self.owner = owner
        self.plate = plate
        self.passengers = []
        self.location = []


    def get_passengers(self):
        return self.passengers

    def get_ap_mac(self):
        return self.ap_mac

    def get_owner(self):
        return self.owner

    def get_location(self):
        return self.location



    def get_plate(self):
        return self.plate

    def get_chasis_number(self):
        return self.chasis_number

    def set_passengers(self,passenger):
        self.passengers.append(passenger)

    def set_ap_mac(self,mac):
        self.mac = mac


    def set_owner(self,owner):
        self.owner = owner

    def set_plate(self,plate):
        self.plate = plate

    def set_chasis_number(self,cn):
        self.chasis_number = cn

    def set_location(self,location):
        self.location.append(location)



# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 17:57:44 2018

@author: Tanmay
"""

class owner:
    def __init__(self,name,add,mobile,ssos):
        self.name = name
        self.add = add
        self.mobile = mobile
        self.ssos = ssos

    def get_name(self):
        return self.name
    def get_mobile(self):
        return self.mobile
    def get_add(self):
        return self.add
    def get_ssos(self):
        return self.ssos



class Passenger:
    def __init__(self,username,phone, name = None, dob=None, gender=None, ssos=None,pwd = None):

        if(name!=None):


            self.name = name
            self.dob = dob
            self.username = username
            self.phone = phone
            self.gender = gender
            self.ssos = ssos
            self.travels = []
            self.pwd = pwd




    def get_name(self):
        return self.name
    def get_dob(self):
        return self.dob
    def get_gender(self):
        return self.gender
    def get_ssos(self):
        return self.ssos
    def get_username(self):
        return self.username
    def get_mobile(self):
        return self.mobile

    def set_username(self,username):
        self.username=username
    def set_mobile(self,mobile):
        self.phone = mobile

    def get_travels(self):
        return self.travels
    def get_pwd(self):
        return self.pwd
    def set_pwd(self,pwd):
        self.pwd = pwd

    def set_name(self,name):
        self.name = name
    def set_dob(self,dob):
        self.dob = dob
    def set_gender(self,gender):
        self.gender = gender
    def set_ssos(self,ssos):
        self.ssos = ssos
    def set_travels(self,travel):
        self.travels.append(travel)




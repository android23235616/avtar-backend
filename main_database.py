# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 23:34:51 2018

@author: Tanmay
"""
import os
from os import listdir
import passenger
import pickle
import time
import vehicle
import location
from ml import take_data
import travels
import json
import owner
import emergency
from flask import Flask,render_template,url_for,redirect
from flask import request

my_key = 'AIzaSyCqT_1BtmlMw09HypO7L0EFRIIkBPtlz2Q'



app = Flask(__name__,template_folder='./templates')

app.config.update(
    DEBUG=True,
    TEMPLATES_AUTO_RELOAD=True
)




vehicle_dir = "./vehicle"

emergency_dir = "./emergency_dir"
owner_dir = "./owner"
passenger_dir = "./passenger"
def initialise():


    if(not os.path.exists(vehicle_dir)):
        os.mkdir(vehicle_dir)
    if(not os.path.exists(owner_dir)):
        os.mkdir(owner_dir)
    if(not os.path.exists(passenger_dir)):
        os.mkdir(passenger_dir)

    if(not os.path.exists(emergency_dir)):
        os.mkdir(emergency_dir)

def load_file(file_name,objects,sos=False):
     if(objects==owner.owner):
        path = os.path.join(owner_dir,file_name)
     elif(objects==passenger.Passenger and not sos):
        path = os.path.join(passenger_dir,file_name)
     elif(objects==vehicle.Vehicle):
        path = os.path.join(vehicle_dir,file_name)
     elif(sos):
         path = os.path.join(emergency_dir,file_name)
     elif(objects==emergency.Emergency):
          path = os.path.join(emergency_dir,file_name)


     f = open(path,"rb")
     b = pickle.load(f)
     f.close()
     return b

def save_file(objects,sos=False):



    if(type(objects)==owner.owner):
        path = os.path.join(owner_dir,objects.get_ssos())
    elif(type(objects)==passenger.Passenger and not sos):
        path = os.path.join(passenger_dir,objects.get_ssos())
    elif(type(objects)==vehicle.Vehicle):
        path = os.path.join(vehicle_dir,objects.get_chasis_number())
    elif(sos):
        path = os.path.join(emergency_dir,objects.get_ssos())
    elif(type(objects)==emergency.Emergency):
        path = os.path.join(emergency_dir,objects.get_id())



    if(os.path.exists(path)):
        f = open(path,"wb")
        del(f)

    f = open(path,"wb")
    pickle.dump(objects,f)
    f.close()


def save_sos(ssos,chesis):
    p = load_file(ssos,passenger.Passenger)
    v = load_file(chesis,vehicle.Vehicle)
    temp = emergency.Emergency(p,v)
    save_file(temp)

    return "1"

def load_sos():
    result = []
    for f in listdir(emergency_dir):
        minTemp = {}
        tempEmerg = load_file(str(f),emergency.Emergency)
        tempPassenger = tempEmerg.get_victim()
        tempVehicle = tempEmerg.get_vehicle()
        minTemp["name"] = tempPassenger.get_name()
        minTemp["dob"] = tempPassenger.get_dob()
        minTemp["gender"] = tempPassenger.get_gender()
        minTemp["chesis"] = tempVehicle.get_chasis_number()
        minTemp["ssos"] = tempPassenger.get_ssos()
        minTemp["id"] = str(f)
        result.append(minTemp)
    return json.dumps(result)



initialise()
#==============================================================================
#o1 = owner.owner('kuli','a1','m1','o1')
#
#v1 = vehicle.Vehicle('v1','a1',o1,'p1')
#
#save_file(v1)
#
#==============================================================================

#==============================================================================
#==============================================================================

#p1 = passenger.Passenger('tanmay','dob','m','ssos')
#
#save_file(p1)

def startJourney(chasis,ssos_passenger,lat,lng):
    p1 = load_file(ssos_passenger,passenger.Passenger)
    locationStart = location.location(str(time.strftime("%c")),lat,lng)
    t1 = travels.Travels(chasis,locationStart)
    p1.set_travels(t1)
    save_file(p1)
    v1 = load_file(chasis,vehicle.Vehicle)
    v1.set_passengers(p1)
    save_file(v1)
    return str(v1.get_ap_mac())


def stopJourney(chasis,ssos_passenger,lat,lng):
    p1 = load_file(ssos_passenger,passenger.Passenger)
    locationStop = location.location(str(time.strftime("%c")),lat,lng)
    t1 = p1.get_travels()
    t1 = t1[len(t1)-1]
    t1.set_timeStop(locationStop)
    p1.set_travels(t1)
    save_file(p1)


def setowner(name,add,mobile,ssos):
    o1 = owner.owner(name,add,mobile,ssos)
    save_file(o1)

def setpassenger(ssos,username=None,mobile=None,name=None,dob=None,gender=None,pwd=None):
    p = passenger.Passenger(username,mobile,name,dob,gender,ssos,pwd)
    save_file(p)




def add_owners_in_vehicles(chesis,ssos_owner,vehicle_number):
   v = load_file(chesis,vehicle.Vehicle)
   o1 = load_file(ssos_owner,owner.owner)
   v.set_owner(o1)
   v.set_plate(vehicle_number)
   save_file(v)

def add_location_vehicle(chesis,lat,lng):
    v = load_file(chesis,vehicle.Vehicle)
    lo = location.location(time.strftime("%c"),lat,lng)
    v.set_location(lo)
    save_file(v)



def add_vehicle_chesis(chesis,ap):
    v = vehicle.Vehicle(chesis,ap)
    save_file(v)


def add_passenger_profile(pwd,name,dob,gender,ssos):
    p = passenger.Passenger(name,dob,gender,ssos,pwd)
    save_file(p)


def get_mac(chesis):
    b = load_file(chesis,vehicle.Vehicle)
    result = b.get_ap_mac()
    return str(result)

def get_last_location(chesis):
    b = load_file(chesis,vehicle.Vehicle)
    o1 = b.get_owner()
    name = str(o1.get_name())
    add = str(o1.get_add())
    mobile =str(o1.get_mobile())
    loc = b.get_location()
    result = ""
    locations = []
    for e in loc:
        temp = {}
        temp["lat"] = e.getLat()
        temp["lng"] = e.getLng()
        temp["time"] = e.getTimeStamp()
        temp["name"] = name
        temp["add"] = add
        temp["mobile"] = mobile

        locations.append(temp)



    result = json.dumps(locations)


    return result
def get_real_location(chesis):
    bs= load_file(chesis,vehicle.Vehicle)
    temp = {}
    loc = bs.get_location()
    ow = bs.get_owner()
    name = ow.get_name()
    add = ow.get_add()
    mobile = ow.get_mobile()
    b = loc[len(loc)-1]

    temp["lat"] = b.getLat()
    temp["lng"] = b.getLng()
    temp["name"] = name
    temp["add"] = add
    temp["mobile"] = mobile
    return json.dumps(temp)


@app.route('/get_real_location',methods=['POST','GET'])

def get11():
    if(request.method=='GET'):
        last = get_real_location(request.args.get('chesis'))



        return (last)
    else:

        return "0"


def get_passenger_journey_status(ssos):
    p = load_file(ssos,passenger.Passenger)
    temp = p.get_travels()
    t = temp[len(temp)-1]
    try:
        return str(t.get_timeStop().getLat())
    except:
        return "-1"


@app.route('/tracking')

def get12():
    return render_template('faltu2.html')

@app.route('/owner',methods=['POST','GET'])
def owners():
    if(request.method=='GET'):
        setowner(request.args.get('name'),request.args.get('add'),request.args.get('mobile'),request.args.get('ssos'))
        return "1"
    else:
        return "0"


@app.route('/get_mac',methods=['POST','GET'])

def get2():
    if(request.method=='GET'):
        result = get_mac(request.args.get('chesis'))
        return result
    else:
        return 0

@app.route('/passenger',methods =  ['POST','GET'])

def passengers():
    if(request.method=='GET'):
        #setpassenger(ssos,username,mobile,name,dob,gender,pwd):

        setpassenger(request.args.get('ssos'),request.args.get('username'),request.args.get('mobile'),request.args.get('name'),request.args.get('dob'),request.args.get('gender'),request.args.get('pwd'))
        return "1"

    else:
        return "0"



@app.route('/emergency')

def get4():
    return load_sos()

@app.route('/sos',methods= ['POST','GET'])

def add8():
    if(request.method=='GET'):
        return save_sos(request.args.get('ssos'),request.args.get('chesis'))
    else:
        return "0"

@app.route('/add_vehicle',methods = ['POST','GET'])
def add():
    if(request.method=='GET'):
        add_vehicle_chesis(request.args.get('chesis'),request.args.get('ap'))
        return "1"
    else:
        return "0"

@app.route('/journey',methods = ['POST','GET'])

def get23():
    if(request.method=='GET'):
        return get_passenger_journey_status(request.args.get('ssos'))


@app.route('/get_location',methods=['POST','GET'])

def get1():
    if(request.method=='GET'):
        last = get_last_location(request.args.get('chesis'))



        return (last)
    else:

        return "0"

@app.route('/passenger_username',methods=['POST','GET'])

def username():
    if(request.method=='GET'):
        p = load_file(request.args.get('ssos'),passenger.Passenger)
        return p.get_username()



@app.route('/add_vehicle_details',methods = ['POST','GET'])
def add2():
    if(request.method=='GET'):
        add_owners_in_vehicles(request.args.get('chesis'),request.args.get('ssos_owner'),request.args.get('lic'))
        return "1"
    else:
        return "0"


def delete_sos(ids):
    path = os.path.join(emergency_dir,ids)

    os.remove(path)



@app.route('/a')
def hello():
    return "hello"


@app.route('/passenger_enter',methods = ['POST','GET'])

def add4():
    if(request.method=='GET'):
        return startJourney(request.args.get('chesis'),request.args.get('ssos'),request.args.get('lat'),request.args.get('lng'))

    else:
        return "0"

@app.route('/passenger_exit',methods = ['POST','GET'])

def add6():
    if(request.method=='GET'):
        stopJourney(request.args.get('chesis'),request.args.get('ssos'),request.args.get('lat'),request.args.get('lng'))
        return "1"
    else:
        return "0"
@app.route('/vehicle_location',methods = ['POST','GET'])

def add5():
    if(request.method=='GET'):
        add_location_vehicle(request.args.get('chesis'),request.args.get('lat'),request.args.get('lng'))
        return "1"
    else:
        return "0"
@app.route('/admin_panel')

def admin():
    #return "hello admin"

    return render_template('faltu.html')



@app.route('/my_thread2.js')

def admin3():
    #return "hello admin"
    return render_template('my_thread2.js')



@app.route("/")
def mapview():
    return render_template('faltu.html')

@app.route("/analysis",methods = ['POST','GET'])

def analyse():
    if(request.method=='GET'):
        try:
            return take_data(str(request.args.get('lat')),str(request.args.get('lng')),request.args.get('time'))
        except:
            return take_data(str(request.args.get('lat')),str(request.args.get('lng')))

@app.route('/index')

def myindex():
    return render_template('search.html')

@app.route('/static/style.css')

@app.route('/my_thread.js')

def admin2():
    #return "hello admin"
    return render_template('my_thread.js')



def first_css():

    return render_template('style.css')

@app.route('/index2',methods = ['POST','GET'])

def myindex2():
    if(request.method=='GET'):

        return render_template('index2.html',chesis = request.args.get('s'))

@app.route('/view')

def view_sos():
    return render_template('sos.html')


@app.route('/delete',methods = ['POST','GET'])

def delete():
    if(request.method=='GET'):
        delete_sos(request.args.get('id'))
        return redirect(url_for('view_sos'))


if __name__ == '__main__':

    app.run(debug = True)

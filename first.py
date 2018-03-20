from sklearn import linear_model,svm

import tensorflow as tf

import pandas as pd

import numpy as np

from sklearn import cross_validation

df = pd.read_csv('data.csv')

asd = df['area']

rapes = df['NUM']



times = {'M':1,'N':2,"E":3,"MN":4}


def normalize(x):

    return np.tanh(x)

    temp = np.array(rapes)
    x_new = (x - min(temp))/(max(temp)-min(temp))
    return x_new


area_index = {}

for i in range(len(asd)):
    area_index[asd[i]] = len(area_index)
    i+=30


x_data = []
y = []
for area,time,r in zip(df['area'],df['Y'],df['NUM']):
    a = [area_index[area],times[time]]
    b = normalize(r)
    x_data.append(a)
    y.append(b)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x_data,y,test_size=0.1)

x = tf.placeholder(tf.float32)
y = tf.placeholder(tf.float32)

fact = tf.constant(0.0182)

W = tf.Variable((tf.random_normal([1700,3000])*fact),dtype = tf.float32)
B = tf.Variable(tf.zeros([1700,1])+0.1,dtype = tf.float32)



linear_model_ =tf.nn.relu(tf.add(tf.matmul(W,x),B))

W2 = tf.Variable((tf.random_normal([3000,1700])*fact),dtype = tf.float32)
B2 = tf.Variable(tf.zeros([3000,1])+0.1,dtype = tf.float32)


linear_model =((tf.add(tf.matmul(W2,linear_model_),B2)))

#linear_model = W*x+B
loss = tf.square(y-linear_model)
loss = tf.reduce_mean(tf.reduce_sum(loss))

optimiser = tf.train.AdamOptimizer(0.01)
train = optimiser.minimize(loss)
madar = None





with tf.Session() as sess:
    init  = tf.global_variables_initializer()
    sess.run(init)

    xs = np.linspace(-100,100,3000).reshape(3000,1)
    ys = np.square((xs))+np.random.normal(0,300,(3000,1))


    plt.ion()
    for i in range(300000):
       # runner =
        if(i%50!=0):

           madar = sess.run(linear_model,{x:xs,y:ys})

           [_,__,lm] =(sess.run([train,loss,linear_model],{x:xs,y:ys}))


           plt.scatter(xs.ravel(),lm.ravel(),s=.2)
           plt.pause(0.001)
           plt.clf()


        else:


            [_,l]=sess.run([train,loss],{x:xs,y:ys})
            print("At "+str(i)+" loss is "+str(l))


    print(sess.run([W,B]))
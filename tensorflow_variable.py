'''
Code Wriiten by : KEERTHI KUMAR K.G
'''
#Tensorflow Variable Program
#Importing the Tensorflow Library
#Buiding the graph
###
import tensorflow as tf

x1 = tf.Variable(6,name = 'x1')#Creating a Tensor Variable
x2 = tf.Variable(4,name = 'x2')#Creating another Tensor Variable

print x1,x2

#Through this line of code we are initializing the variables in
#the dataflow graph
init = tf.global_variables_initializer()

###

###
#Runing the graph or the session
with tf.Session() as sess:
    sess.run(init) #Running our Variable initialization
    a = sess.run(x1)
    b = sess.run(x2)
    print a,b

###

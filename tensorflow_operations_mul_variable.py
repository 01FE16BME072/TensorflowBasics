'''
Code Wriiten by : KEERTHI KUMAR K.G
'''
#Basic Mathematical Operations with Tensorflow Placeholder
#Importing the Tensorflow Library
###
#Building the graph
import tensorflow as tf
'''
Now we can even also say to which datatype our Tensor will belong to
by just writting something like the code  below

x = tf.Variable(65,name = 'var1',dtype = tf.float64)
So here dtype = tf.float64 makes out x Variable Tensor as
a float type

'''
a = tf.Variable(56,name = 'mult1')#Creating a Tensor Variable
b = tf.Variable(100,name = 'mult2')#Creating another Tensor Variable

c = a * b #Multiplication through operands
d = tf.multiply(a,b)#Multiplication through inbuilt functions

print c
print d

#This Line of code helps in initializing all the variabels
init = tf.global_variables_initializer()
###

###
#Running the graph or Session
with tf.Session() as sess:
    sess.run(init)
    x = sess.run(c)
    y = sess.run(d)
print x
print y

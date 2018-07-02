'''
Code Wriiten by : KEERTHI KUMAR K.G
'''
#Basic Mathematical Operations with Tensorflow Placeholder
#Importing the Tensorflow Library
###
#Building the graph
import tensorflow as tf

a = tf.constant(6,name = 'div1',dtype = tf.float64)#Creating a Tensor Constant of float datatype
b = tf.constant(3,name = 'div2',dtype = tf.float64)#Creating another Tensor Constant of float datatype

c = a / b #By using simple operand methods
d = tf.div(a,b)#By using the inbuilt function written in Tensorflow

print c
print d
###
###
#Running the graph or Session
with tf.Session() as sess:
    x = sess.run(c)
    y = sess.run(d)
print x
print y
###

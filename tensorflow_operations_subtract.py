'''
Code Wriiten by : KEERTHI KUMAR K.G
'''
#Basic Mathematical Operations with Tensorflow Placeholder
#Importing the Tensorflow Library
###
#Building the graph
import tensorflow as tf

a = tf.placeholder(dtype = tf.float64)#Creating a Tensor Placeholder
b = tf.placeholder(dtype = tf.float64)#Creating another Tensor Placeholder

c = a - b #By using simple operand
d = tf.subtract(a,b) #By using built-in function present in Tensorflow

print c
print d
###
###
#Running the graph or Session
with tf.Session() as sess:
    x = sess.run(c,feed_dict = {a : 10,b : 5})
    y = sess.run(d,feed_dict = {a : 10,b : 5})
print x
print y
###

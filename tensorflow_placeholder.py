'''
Code Wriiten by : KEERTHI KUMAR K.G
'''
#Tensorflow Placeholder Program
#Importing the Tensorflow Library
###
#Building the Graph
import tensorflow as tf

x1 = tf.placeholder(tf.int64,name = 'x1')#Creating a Tensor Placeholder
x2 = tf.placeholder(tf.int64,name = 'x2')#Creating another Tensor Placeholder

print x1,x2
###
###
#Running the graph or the session
with tf.Session() as sess:
    a = sess.run(x1,feed_dict = {x1:9})#Passing the value to the Tensor Placeholder as a dictionary
    b = sess.run(x2,feed_dict = {x2:5})#Passing the value to the Tensor Placeholder as a dictionary

    print a,b
###

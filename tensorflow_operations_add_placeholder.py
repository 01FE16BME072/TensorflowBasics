'''
Code Wriiten by : KEERTHI KUMAR K.G
'''
#Basic Mathematical Operations with Tensorflow Placeholder
#Importing the Tensorflow Library
###
#Building the graph
import tensorflow as tf

a = tf.placeholder(tf.float64)#Creating a Tensor Placeholder
b = tf.placeholder(tf.float64)#Creating another Tensor Placeholder

c = a + b #Adding by normal operand method
d = tf.add(a,b)#Adding through the Tensorflow Library Function
#tf.add() method is the best one compared to the other operand method
'''
We can also use other Operations like multiplication,division,subtraction
on our tensors either by using the operands or by using the built-in
functions in the tensorflow library.But more oftenly we use the built-in
methods to give us a better result
'''
print c
print d
###

###
#Running the Session or graph

with tf.Session() as sess:
    x = sess.run(c,feed_dict = {a : 6,b : 6 })
    y = sess.run(d,feed_dict = {a : 6,b : 6 })

print x
print y
###

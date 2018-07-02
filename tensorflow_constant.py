'''
Code Wriiten by : KEERTHI KUMAR K.G
'''

#Tensorflow Constant Program
'''
x1 = 3
x2 = 7

print x1,x2
print x1 + x2

This is how we do in general in either python2 or python3
But while using tensorflow things change a little bit so keerthi is
going to do it
'''
#Importing the tensorflow Library
####
import tensorflow as tf

x1 = tf.constant(3,name = 'x1')#Creating a Tensor Constant
x2 = tf.constant(7,name = 'x2')#Creating another Tensor Constant

print x1
print x2
####
'''

Upto this line of code we are justing creating a tensorflow constant
in a dataflow graph that means only building of graph takes place

So in the next set of line code we will be running the session of the
graph which we previously initialized

'''
with tf.Session() as sess:
    a = sess.run(x1)
    b = sess.run(x2)
    print a,b

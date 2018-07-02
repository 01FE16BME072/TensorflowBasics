'''
Code Wriiten by : KEERTHI KUMAR K.G
'''
#Lets start applying little more complex operation to the Tensor datastructure
#Now here we will be trying to find the determinant of a given matrix

#Importing the required Libraries
import tensorflow as tf
import numpy as np

matrixA = np.array([(4,5,6),(7,3,2),(1,8,6)],dtype = np.float64)#Creating a numpy array

determinant_matrixA = tf.matrix_determinant(matrixA)#Finding the determinant using the inbuilt function

with tf.Session() as sess:
    result = sess.run(determinant_matrixA)
print 'The determinant of the given Matrix is: ',result #Printing the result after running the Session

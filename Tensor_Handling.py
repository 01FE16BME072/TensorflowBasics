'''
Code Wriiten by : KEERTHI KUMAR K.G
'''
#Lets start applying little more complex operation to the Tensor datastructure
#We will do this by considering two matrices and applying various operation on them

#Importing the required libraries
import tensorflow as tf
import numpy as np

matrixA = np.array([(2,2,2),(4,4,4),(6,6,6)],dtype = np.float64)#Lets consider an array of float datatype
matrixB = np.array([(1,1,1),(3,3,3),(5,5,5)],dtype = np.float64)#Lets consider another array of the same datatype

print 'FirstMatrix is :',matrixA
print 'SecondMatrix is :',matrixB

tensorA = tf.constant(matrixA,name = 'matrixA')#Creatina a Tensor constant and the value given to that will be the array value which we already declared(matrixA)
tensorB = tf.constant(matrixB,name = 'matrixB')#Creatina a Tensor constant and the value given to that will be the array value which we already declared(matrixB)

matrix_multiplication = tf.matmul(tensorA,tensorB)#This is a function in Tensorflow library which helps us in doing matrix multiplication
matrix_add = tf.add(tensorA,tensorB)#This function just adds the two matrix

with tf.Session() as sess:
    result1 = sess.run(matrix_multiplication)
    result2 = sess.run(matrix_add)

print 'The Addition of two matrices is: ',result2
print 'The Matrix Multiplication of two matrices is: ',result1

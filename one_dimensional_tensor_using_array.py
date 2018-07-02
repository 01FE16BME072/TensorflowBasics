'''
Code Wriiten by : KEERTHI KUMAR K.G
'''
#Converting from Array to Tensor tensorflow
#We can also even 2d,3d Tensor using this methods
#Importing the required libraries
import tensorflow as tf
import numpy as np

array_1d = np.array([4,5,8,9],dtype = np.float64)#This line of code just helps us in creating an Array of float datatype
print array_1d
'''
Tensors can be identified by three parameters:
1.Rank(a rank is known as order or n-dimensions of a tensor)
2.Shape(Shape is nothing but the number of rows and columns the Tensor Contains)
3.Type(Datatype assigned to each tensor elements)
'''
print array_1d.ndim #This prints the dimension of my array(Rank in Tensor)

print array_1d.shape #This prints the shape of my array(Shape in Tensor)

print array_1d.dtype #This prints the datatype of my array(type in Tensor)

#The below line of code converts our array into  a Tensor of float datatype
tensor_tensorflow_1d = tf.convert_to_tensor(array_1d,dtype= tf.float64)
print tensor_tensorflow_1d #Printing the converted Tensor before running the session


with tf.Session() as sess:
    tensor = sess.run(tensor_tensorflow_1d)
print tensor #Printing the converted Tensor after running the Session

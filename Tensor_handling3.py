'''

TensorFlow is designed to handle tensors of all sizes and operators that can be used to
manipulate them. In this example, in order to see array manipulations, we are going to
work with a digital image. As you probably know, a color digital image that is a MxNx3
size matrix (a three order tensor), whose components correspond to the components of red,
green, and blue in the image (RGB space), means that each feature in the rectangular box for
the RGB image will be specified by three coordinates, i, j, and k.

You can see visualisation of this in this folder only just open refrence_image.png

'''
#Importing the required Libraries
import tensorflow as tf
import matplotlib.image as image #This library is used for reading and showing the image on the screen here you can even replace this with the opencv library
from matplotlib import pyplot as plt

read_img = image.imread("refrence_image.png")

plt.imshow(read_img)
plt.show()
#Now here if we want then we can even see the rank and the shape

read_tensor_img = tf.placeholder("uint8",[None,None,4])

slice_read_tensor_img = tf.slice(read_tensor_img,[100,0,0],[200,200,-1])

with tf.Session() as sess:
    slicing = sess.run(slice_read_tensor_img,feed_dict = {read_tensor_img:read_img})
plt.imshow(slicing)
plt.show()

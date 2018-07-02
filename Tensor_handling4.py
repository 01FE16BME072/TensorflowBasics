#Transposing an image using Tensors in Tensorflow

import tensorflow as tf
import matplotlib.image as image
from matplotlib import pyplot as plt

read_img = image.imread("refrence_image.png")

plt.imshow(read_img)
plt.show()

tensor_read_img = tf.Variable(read_img)
'''
To perform the transpose of our matrix, we use the transpose function of TensorFlow. This
method performs a swap between the axes 0 and 1 of the input matrix, while the z axis is
left unchanged
'''
transpose_tensor_read_img = tf.transpose(tensor_read_img,perm = [1,0,2])

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    result = sess.run(transpose_tensor_read_img)

plt.imshow(result)
plt.show()

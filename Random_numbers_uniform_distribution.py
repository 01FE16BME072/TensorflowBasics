import tensorflow as tf
from matplotlib import pyplot as plt

uniform_random = tf.random_uniform([10],minval = 0,maxval = 2)

with tf.Session() as sess:
    result = sess.run(uniform_random)
    plt.hist(result,normed = True)
    plt.show()
print result

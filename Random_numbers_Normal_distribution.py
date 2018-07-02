import tensorflow as tf
from matplotlib import pyplot as plt

normal_distribution_value = tf.random_normal([100],mean = 0,stddev= 1)

with tf.Session() as sess:
    result = sess.run(normal_distribution_value)
    plt.hist(result,normed = True)
    plt.show()
print result

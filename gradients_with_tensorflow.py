'''
we will use Tensorflow for a  mathematical operator that calculates the derivative of y with respect to its expression x
parameter. For this purpose, we use the tf.gradients() function.
Let us consider the math function y = x**2 . We want to compute the gradient y with
respect to x=1 . So Lets do it:
'''
import tensorflow as tf

x = tf.placeholder(tf.float64)

y = tf.square(x)

derivative_of_y_wrt_x = tf.gradients(y,x)

with tf.Session() as sess:
    result = sess.run(derivative_of_y_wrt_x,feed_dict = {x : 1 })

print 'Derivative of y with respect to x at x = 1 is :',result

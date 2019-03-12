import tensorflow as tf


x = tf.Variable([1, 2])
a = tf.constant([3, 3])

sub = tf.subtract(x, a)  # 减法操作
add = tf.add(x, sub)  # 加法操作

init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    print(sess.run(sub))
    print(sess.run(add))


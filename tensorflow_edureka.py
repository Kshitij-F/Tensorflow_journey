# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 14:22:21 2018

@author: Horizon
"""
import tensorflow as tf

a = tf.constant(5)
b = tf.constant(6)

c = a*b

sess = tf.Session()

file_writer = tf.summary.FileWriter('C:\Tensor\Tensorflow-Bootcamp-master\graph', sess.graph)
output = sess.run(c)
print (output)
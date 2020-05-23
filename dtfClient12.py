#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:03:22 2018

@author: xyli
"""

import tensorflow as tf
import numpy as np


train_x = np.linspace(-1,1,1001)
train_y=2 * train_x + np.random.randn(*train_x.shape) * 0.33 +10

X = tf.placeholder("float")
Y = tf.placeholder("float")
w = tf.Variable(0.0, name="weight")
b = tf.Variable(0.0, name="reminder")

init_op = tf.global_variables_initializer()

cost_op = tf.square(Y-tf.multiply(X,w)-b)
train_op = tf.train.GradientDescentOptimizer(0.01).minimize(cost_op)

with tf.Session("grpc://127.0.0.1:2222") as sess:
    with tf.device("/job:worker/task:0"):
        sess.run(init_op)

        for i in range(1000):
            for(x,y) in zip(train_x,train_y):
                sess.run(train_op,feed_dict={X:x,Y:y})
        print(sess.run(w))
        print(sess.run(b))


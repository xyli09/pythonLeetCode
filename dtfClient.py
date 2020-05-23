#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 16:03:22 2018

@author: xyli
"""

import tensorflow as tf

c=tf.constant("Hello, Distribute TensorFlow!")

server_target="grpc://localhost:55697"

sess=tf.Session(server_target)

print(sess.run(c))

sess.close()
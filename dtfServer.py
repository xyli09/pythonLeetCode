#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:32:08 2018

@author: xyli
"""

import tensorflow as tf

print(tf.__version__)




#c=tf.constant("Hello! Distribute TensorFlow")

server=tf.train.Server.create_local_server()

server.join()

#sess=tf.Session(server.target)



#print(sess.run(c))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 15:32:08 2018

@author: xyli
"""

import tensorflow as tf

print(tf.__version__)


worker1 = "localhost:2222"
worker2 = "localhost:2223"

worker_hosts = [worker1, worker2]

cluster_spec = tf.train.ClusterSpec({ "worker": worker_hosts})

server = tf.train.Server(cluster_spec, job_name="worker", task_index=1)
server.join()

#c=tf.constant("Hello! Distribute TensorFlow")

# server=tf.train.Server.create_local_server()

# server.join()

#sess=tf.Session(server.target)



#print(sess.run(c))
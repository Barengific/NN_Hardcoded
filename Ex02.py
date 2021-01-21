# -*- coding: utf-8 -*-
"""
@author: barengific
"""

import numpy as np

#single neuron
ins = [1.0, 2.0, 3.0, 2.5]
ws = [0.2, 0.8, -0.5, 1.0]
bias = 2.0
outs = np.dot(ws, ins) + bias
#print(outs)


#layer of neurons
ws = [[0.2, 0.8, -0.5, 1],
      [0.5, -0.91, 0.26, -0.5],
      [-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]
layer_outs = np.dot(ws, ins) + biases
print(layer_outs)


ins = [[1.0, 2.0, 3.0, 2.5],
       [2.0, 5.0, -1.0, 2.0],
       [-1.5, 2.7, 3.3, -0.8]]
ws = [[0.2, 0.8, -0.5, 1.0],
      [0.5, -0.91, 0.26, -0.5],
      [-0.26, -0.27, 0.17, 0.87]]
biases = [2.0, 3.0, 0.5]
layer_outs = np.dot(ins, np.array(ws).T) + biases
print(layer_outs)



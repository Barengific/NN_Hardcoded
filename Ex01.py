# -*- coding: utf-8 -*-
"""

@author: barengific
"""
#basic single neuron
ins = [1,2,3]
ws = [0.2, 0.8, -0.5]
bias = 2
out = (ins[0]*ws[0] +
       ins[1]*ws[1] +
       ins[2]*ws[2] + bias)
#print(out)

#basic single neuron+
ins = [1.0, 2.0, 3.0, 2.5]
ws = [0.2, 0.8, -0.5, 1.0]
bias = 2.0
out = (ins[0]*ws[0] +
       ins[1]*ws[1] +
       ins[2]*ws[2] +
       ins[3]*ws[3] + bias)
#print(out)

#three neurons
ins = [1, 2, 3, 2.5]
ws1 = [0.2, 0.8, -0.5, 1]
ws2 = [0.5, -0.91, 0.26, -0.5]
ws3 = [-0.26, -0.27, 0.17, 0.87]
bias1 = 2
bias2 = 3
bias3 = 0.5
out = [
       # Neuron 1:
           ins[0]*ws1[0] +
           ins[1]*ws1[1] +
           ins[2]*ws1[2] +
           ins[3]*ws1[3] + bias1,
       # Neuron 2:
           ins[0]*ws2[0] +
           ins[1]*ws2[1] +
           ins[2]*ws2[2] +
           ins[3]*ws2[3] + bias2,
       # Neuron 3:
           ins[0]*ws3[0] +
           ins[1]*ws3[1] +
           ins[2]*ws3[2] +
           ins[3]*ws3[3] + bias3]
#print(out)


ins = [1, 2, 3, 2.5]
ws = [[0.2, 0.8, -0.5, 1],
      [0.5, -0.91, 0.26, -0.5],
      [-0.26, -0.27, 0.17, 0.87]]
biases = [2, 3, 0.5]

# Output of current layer
layer_out = []

# For each neuron
for n_ws, n_bias in zip(ws, biases):
    # Zeroed output of given neuron
    n_out = 0
    # For each input and weight to the neuron
    for n_ins, w in zip(ins, n_ws):
        # Multiply this input by associated weight
        # and add to the neuron’s output variable
        n_out += n_ins*w
    # Add bias
    n_out += n_bias
    # Put neuron’s result to the layer’s output list
    layer_out.append(n_out)
print(layer_out)








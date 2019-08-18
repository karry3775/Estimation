#############
# SIMPLE IMPLEMENTATION OF KALMAN FILTER
#############
from __future__ import division
import numpy as np

# define the initial information
dt = 0.5
#motion model
F = np.array([[1, dt],
              [0, 1]])
#measurement matrix
G = np.array([[0, dt]]).T
#Initial Uncertainty in state
P = np.array([[0.01, 0],
               [0, 1]])
# Motion noise
Q = np.array([[0.1, 0],
              [0, 0.1]])
#Measurement noise
R = np.array([[0.05]])
#initial state
x = np.array([[0, 5]]).T

#measurement model H
H = np.array([[1,0]])

#control signal
u = -2

#measurement
y = 2.2
#PREDICTION
x = F.dot(x) + G.dot(u)
P = F.dot(P).dot(F.T) + Q
print("P: {}".format(P))

#CALCULATION OF OPTIMAL GAIN
K = P.dot(H.T).dot(np.linalg.inv(H.dot(P).dot(H.T) + R))
print("K: {}".format(K))

#CORRECTION STEP
x = x + K.dot(y - H.dot(x))
P = (np.eye(2) - K.dot(H)).dot(P)

#printing values
print("x: {}".format(x))
print("P: {}".format(P))

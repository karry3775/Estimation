########
# BASIC CODE FOR ESTIMATION OF MEASUREMENTS USING LEAST SQUARES
########
from collections import OrderedDict
import matplotlib.pyplot as plt
import numpy as np

data = np.array([[1000,1200,998,800,400]]).T
for i in range(len(data)):
    plt.plot(i,data[i],'rx',label="MEASURED VALUE")

H = np.array([[1,1,1,1,1]]).T
k = np.matmul(H.T,H)
p = np.linalg.inv(k)
# print(np.matmul(np.array(1/(int(np.matmul(H.T,H)))),H.T))
estimate = np.matmul(np.matmul(p,H.T),data)
plt.plot(i,estimate,'cx',label="ESTIMATED VALUE")
"""
TO PREVENT REPEATED LABELS FOR SAME LABEL TAG
"""
handles, labels = plt.gca().get_legend_handles_labels()
by_label = OrderedDict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.show()

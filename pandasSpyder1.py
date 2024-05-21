# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import matplotlib.pyplot as plt
a = [0,1, 2, 3, 4,5,6,7,8,9]
b = [9,9,9,9,9,9,9,9,9,9]
plt.plot(a,b,c='orange',linestyle='dotted')
plt.plot(a,b,c='orange',linestyle='dashed',linewidth=5)
plt.scatter(a,b,c='g',marker='2')
plt.barh(a,b,color='blue')
plt.bar(a,b,color='r')
plt.title('sample graph')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.savefig(r'C:\Users\LENOVO\Desktop\mt\sample.png')
plt.show()
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 13:39:39 2019

@author: snyderd
"""

# print("Hello World! How are you?")

import numpy as np

# for 1D particles

Npart = 10

# initial values: empty lists for each quantity
m = np.zeros(Npart)
v = np.zeros(Npart)
q = np.zeros(Npart)
x = np.zeros(Npart)
T = np.zeros(Npart)

for i in range(0,Npart):
    m[i] = 1.0
    q[i] = 1.0
    x[i] = 0.5*i
    v[i] = 0.2*i
    
    T[i] = 0.5*m[i]*v[i]**2

print(m)
print(q)
print(x)
print(v)

print(T)
    